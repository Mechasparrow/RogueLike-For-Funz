# Purpose: Simple tile to be placed on a map
# tile.py
# Author: Michael Navazhylau

# import libs
import tcod

class Tile:

    # params
    # walkable, can it be walked on
    # blocking, does it block the walking
    # block visible, does it block FOV visibility
    # explored, has the tile been explored by FOV or otherwise?
    def __init__(self, walkable = False, blocking = False, block_visibility = False, explored = False):
        self.walkable = walkable
        self.blocking = blocking
        self.block_visibility = block_visibility
        self.explored = explored
