# Purpose: GameObject with additional behavior and interactivity
# entity.py
# Author: Michael Navazhylau

# import libs
import tcod
from .gameobject import GameObject

# A GameObject in the game's world that interacts with other things with additional behavior
# Extends from GameObject
class Entity(GameObject):

    # params
    # position
    # name
    # Ascii character
    # a color
    # reference to game world
    # combat behavior for combat
    # items for inventory system
    # type of entity

    def __init__(self, x, y, name, chr, color, combat_behavior = None, items = None, game = None, entity_type = "base"):
        GameObject.__init__(self, x, y, name, chr, color, game, type = "Entity")
        self.combat_behavior = combat_behavior
        self.entity_type = entity_type
        self.items = []

        if (self.combat_behavior):
            self.combat_behavior.fighter_name = self.name

    def as_dictionary(self):
        parent_dictionary = super().as_dictionary()

        # Check to see if combat behavior needs to be serialized
        if (self.combat_behavior):
            serialized_combat_behavior = self.combat_behavior.as_dictionary()
        else:
            serialized_combat_behavior = None

        entity_dict = {
            'combat_behavior': serialized_combat_behavior,
            'entity_type': self.entity_type,
            'items': self.items
        }

        merged_dict = {**parent_dictionary, **entity_dict}
        return merged_dict

    def from_dictionary():

        pass

    # move the entity a certain dx and dy
    # can only move on walkable tiles
    def move(self, dx, dy):

        game_map = self.game.floor_manager.get_current_floor().game_map
        (potential_x, potential_y) = self.anticipate_move(dx, dy)

        if (potential_x < game_map.width and potential_x >= 0 and potential_y < game_map.height and potential_y >= 0):
            potential_tile = game_map.tiles[potential_x][potential_y]
            if (potential_tile.walkable == True and potential_tile.blocking == False):
                GameObject.move(self, dx, dy)
