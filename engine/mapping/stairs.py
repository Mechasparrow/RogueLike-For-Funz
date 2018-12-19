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
        self.stairs_behavior = stairs_behavior

    # Use the stairs
    def use_stairs(self):
        print ("using the stairs")
        if (self.stairs_behavior):
            self.stairs_behavior()
