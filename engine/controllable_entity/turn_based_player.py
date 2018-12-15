from .controllable_entity import ControllableEntity

from game import *

class TurnBasedPlayer(ControllableEntity):

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None, turn_handler = None):
        available_actions = [
            "left",
            "right",
            "up",
            "down"
        ]

        ControllableEntity.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, available_actions = available_actions, game = game)
        self.turn_handler = turn_handler

    def control_entity(self, action, callback = None):

        # if player dead dont do anything else
        if (self.combat_behavior.dead or (action not in self.get_actions_available())):
            return

        # By default no turn taken
        turn_taken = False

        # Movement offset from current pos
        dx = 0
        dy = 0

        if (action == "up"):
            dy = -1
        elif (action == "down"):
            dy = 1
        elif (action == "right"):
            dx = 1
        elif (action == "left"):
            dx = -1

        if (dx != 0 or dy != 0):
            turn_taken = True

        (potential_x, potential_y) = self.anticipate_move(dx, dy)

        # Limiting behavior
        safe_to_move = True
        for object in self.game.objects:
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
        for agent in get_game_agents(self.game):
            if (agent.x == potential_x and agent.y == potential_y and not agent.combat_behavior.dead):
                self.combat_behavior.attack(agent.combat_behavior)

        # Pickup behavior
        for gameobject in self.game.objects:
            if (gameobject.x == potential_x and gameobject.y == potential_y):
                if (gameobject.entity_type == "pickup"):
                    pickup = gameobject
                    pickup.pickup_behavior(self)
                    remove_gameobject_from_game(self.game, pickup)

        # Let the game now take a turn
        if (turn_taken and self.turn_handler):
            print ("taking turn")
            self.turn_handler.take_turn()

        # Place player back at top
        if self in self.game.objects:
            player = self
            remove_gameobject_from_game(self.game, player)
            add_gameobject_to_game(self.game, player)
