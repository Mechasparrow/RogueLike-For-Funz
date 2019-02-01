# Purpose: Represent Stairs on the map that can be used to navigate between floors
# stairs.py
# Author: Michael Navazhylau

# import libs
import tcod
from engine.gameobjects import Entity

class Stairs(Entity):

    # params
    # x, y position
    # name of stairs
    # character of stairs
    # color of stairs
    # game ref
    # behavior of stairs when interacted with
    def __init__(self, x, y, name, chr = "^", color = (152, 158, 165), game = None, stairs_behavior = None):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = None, game = game, entity_type = "stairs")

        # PROBLEMATIC FIXME
        self.stairs_behavior = stairs_behavior

    #serialization + parsing
    def as_dictionary(self):
        entity_dictionary = super().as_dictionary()

        #TEMP stairs behavior is function so it can not be serialized
        stairs_dictionary = {
            'stairs_behavior': 'NONE'
        }

        merged_dict = {**entity_dictionary, **stairs_dictionary}
        return merged_dict

    def from_dictionary(dictionary, g):
        # TEMP FIXME default stair behavior is undefined
        return Stairs(x = dictionary['x'], y = dictionary['y'], name = dictionary['name'], chr = dictionary['chr'], color = dictionary['color'], game = g, stairs_behavior = None)

    # Use the stairs
    def use_stairs(self):
        if (self.stairs_behavior):
            self.stairs_behavior()
