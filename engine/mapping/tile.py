
# Code to expand relative imports
import sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

import tcod

from gameconstants import *

class Tile:

    def __init__(self, x, y, blocking = False, block_visibility = False):

        self.x = x
        self.y = y
        self.blocking = blocking
        self.block_visibility = block_visibility

    def draw(self, con):

        if (self.blocking == False):
            # if not a blocking tile, draw a walkable tile
            tcod.console_set_char_background(con, self.x, self.y, color_walkable_tile, tcod.BKGND_SET)
        else:
            # Draw a wall tile
            tcod.console_set_char_background(con, self.x, self.y, color_dark_wall, tcod.BKGND_SET)
