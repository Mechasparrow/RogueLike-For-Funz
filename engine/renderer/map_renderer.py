# Purpose: Util functions for rendering a map
# map_renderer.py
# Author: Michael Navazhylau

# import lib
import tcod

# NOTE not really needed...
import sys
sys.path.append("../..")

# import constants
from gameconstants import *

# Render a map onto the console
def render_map(con, map):

    for x in range(0, map.width):
        for y in range(0, map.height):
            tile = map.getTile(x, y)
            draw_tile(con, x, y, tile, visible = map.fov_map.fov[y][x])

# Clear a map from the console
def clear_map(con, map):

    for x in range(0, map.width):
        for y in range(0, map.height):
            tile = map.getTile(x, y)
            clear_tile(con, x, y, tile)

# Draw a tile to a console at a x, y position
def draw_tile(con, x, y, tile, visible = True):
    if (visible == True):
        # TODO fov code?
        if (not tile.explored == True):
            tile.explored = True

        if (tile.blocking == True):
            # Draw a wall tile
            tcod.console_set_char_background(con, x, y, color_light_wall, tcod.BKGND_SET)
        elif (tile.walkable == True and tile.blocking == False):
            # if not a blocking tile, draw a walkable tile
            tcod.console_set_char_background(con, x, y, color_walkable_tile, tcod.BKGND_SET)
    elif (visible == False):
        if (tile.explored == True):
            if (tile.blocking == True):
                # Draw a wall tile
                tcod.console_set_char_background(con, x, y, color_dark_wall, tcod.BKGND_SET)
            elif (tile.walkable == True and tile.blocking == False):
                # if not a blocking tile, draw a walkable tile
                tcod.console_set_char_background(con, x, y, color_walkable_dark_tile, tcod.BKGND_SET)

    else:
        # if not any of those, draw an empty tile TODO
        return

# Clear a tile at a x,y position
def clear_tile(con, x, y, tile):
    tcod.console_set_char_background(con, x, y, (0,0,0), tcod.BKGND_SET)
