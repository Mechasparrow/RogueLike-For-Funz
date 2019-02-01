# Provides Base Controllable Entity that is controlled through a series of actions
# controllable_entity.py
# Author: Michael Navazhylau

from .controllable_entity import ControllableEntity
from engine.game import GameTurnHandler
from engine.items import Item
from engine.combat import CombatBehavior

# import polyfill
import sys
sys.path.append("..")

# Game utils
from engine.game import *

# TODO serialize + parse

# Uses Controllable Entity as Base
class TurnBasedPlayer(ControllableEntity):

    def __init__(self, x, y, name, chr, color, items = [], combat_behavior = None, game = None, turn_handler = None):
        # predetermined list of action for a turn based player entity
        available_actions = [
            "left",
            "right",
            "up",
            "down"
        ]

        ControllableEntity.__init__(self, x, y, name, chr, color, items = items, combat_behavior = combat_behavior, available_actions = available_actions, game = game)

        # turn handler param to tell the game world to take its turn after the player does
        self.turn_handler = turn_handler

    #serialization + parsing
    def as_dictionary(self):

        controllable_dict = super().as_dictionary()

        turn_handler_dict = self.turn_handler.as_dictionary()

        # NOTE turn handler gotta get serialized and parsed properly
        turn_based_player_dict = {
            'turn_handler': turn_handler_dict
        }

        merged_dict = {**controllable_dict, **turn_based_player_dict}
        return merged_dict

    def from_dictionary(dictionary, g):

        turn_handler = GameTurnHandler.from_dictionary(dictionary['turn_handler'],g)
        parsed_combat_behavior = CombatBehavior.from_dictionary(dictionary['combat_behavior'], g)

        parsed_items = []
        for item_dict in dictionary['items']:
            parsed_items.append(Item.from_dictionary(item_dict, g))

        # NOTE need to parse items + combat_behavior
        return TurnBasedPlayer(x = dictionary['x'], y = dictionary['y'], name = dictionary['name'], chr = dictionary['chr'], color = dictionary['color'], items = parsed_items, combat_behavior = parsed_combat_behavior, game = g, turn_handler = turn_handler)

    # controls the entity based on the actions passed to it
    def control_entity(self, action, callback = None):

        # if the player is dead remove itself and spawn a dead body in its place
        if (self.combat_behavior.dead):
            player = self
            dead_player = player.drop_body()
            remove_gameobject_from_floor(self.game.floor_manager.get_current_floor(), player)
            add_gameobject_to_floor(self.game.floor_manager.get_current_floor(), dead_player)

        # if player dead or no action taken dont do anything else
        if (self.combat_behavior.dead or (action not in self.get_actions_available())):
            return



        # By default no has been taken
        turn_taken = False

        # Movement offset from current pos
        dx = 0
        dy = 0

        # update dx + dy accordingly based off of action
        if (action == "up"):
            dy = -1
        elif (action == "down"):
            dy = 1
        elif (action == "right"):
            dx = 1
        elif (action == "left"):
            dx = -1

        # turn taken if dx or dy is not zero
        if (dx != 0 or dy != 0):
            turn_taken = True

        # anticipate the next position for collision checking
        (potential_x, potential_y) = self.anticipate_move(dx, dy)

        # Limiting behavior
        # Can't move if another gameobject is in the way
        # But if its dead or a pickup, then yeah, we can move
        safe_to_move = True
        for object in self.game.floor_manager.get_current_floor().objects:
            if (object.x == potential_x and object.y == potential_y):
                safe_to_move = False

                if (object.entity_type == "dead_body" or object.entity_type == "pickup"):
                    safe_to_move = True

                if (object.combat_behavior):
                    if (object.combat_behavior.dead):
                        safe_to_move = True


        # Check if the player can actually move
        if (safe_to_move):
            self.move(dx, dy)

        # Attack Behavior
        # TODO generalize to any gameobject
        for agent in get_game_agents(self.game.floor_manager.get_current_floor()):
            if (agent.x == potential_x and agent.y == potential_y and not agent.combat_behavior.dead):
                print ("turn_based_player: Attacking...")
                print (self.combat_behavior.combat_stats.attack)
                self.combat_behavior.attack(agent.combat_behavior)

        # Stair Behavior
        for object in self.game.floor_manager.get_current_floor().objects:
            if (object.entity_type == "stairs" and object.x == potential_x and object.y == potential_y):
                stairs = object
                stairs.use_stairs()

        # Pickup behavior
        # If the gameobject at the next position is a pickup, pick it up
        for gameobject in self.game.floor_manager.get_current_floor().objects:
            if (gameobject.x == potential_x and gameobject.y == potential_y):
                if (gameobject.entity_type == "pickup"):
                    pickup = gameobject
                    pickup.pickup_behavior(self)
                    remove_gameobject_from_floor(self.game.floor_manager.get_current_floor(), pickup)

        # Chest behavior
        # If the gameobject at the next position is a pickup, pick it up
        for gameobject in self.game.floor_manager.get_current_floor().objects:
            if (gameobject.x == potential_x and gameobject.y == potential_y):
                if (gameobject.entity_type == "chest"):
                    chest = gameobject
                    if (chest.opened == False):
                        chest.open_chest(self)
                    else:
                        chest.close_chest()

        # Let the game now take a turn
        if (turn_taken and self.turn_handler):
            self.turn_handler.take_turn()

        # Place player back at top of the game console
        if self in self.game.floor_manager.get_current_floor().objects:
            player = self
            remove_gameobject_from_floor(self.game.floor_manager.get_current_floor(), player)
            add_gameobject_to_floor(self.game.floor_manager.get_current_floor(), player)
