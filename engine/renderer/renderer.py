import tcod

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

from gameconstants import *

class Renderer:

    def __init__(self, game):

        self.console = game.root_console
        self.game = game

    def render_all(self):
        # Render the dashboards
        self.render_dashboards()

        # Render the gameobjects
        self.render_gameobjects()

        # Rendering the map
        self.render_map()

    def update_console(self):
        tcod.console_flush() # Show the console
        pass

    def clear_all(self):
            #clear dashboards
            self.clear_dashboards()

            # clear gameobjects
            self.clear_gameobjects()

            # Clearing the map
            self.clear_map()

    def render_gameobjects(self):
        for object in self.game.objects:
            if (object.entity == True):
                in_fov = self.game.fov_map.fov[object.y][object.x]
                if (in_fov):
                    Renderer.render_gameobject(self.console, object)
            else:
                Renderer.render_gameobject(self.console, object)


    def clear_gameobjects(self):
        for object in self.game.objects:
            Renderer.clear_gameobject(self.console, object)

    def render_gameobject(con, object):
        # Set the color
        tcod.console_set_default_foreground(con, object.color)
        # Draw the object rep on to the console
        tcod.console_put_char(con, object.x, object.y, object.chr, tcod.BKGND_NONE)
        pass

    def clear_gameobject(con, object):
        # Set the color
        tcod.console_set_default_foreground(con, object.color)
        # Draw the object rep on to the console
        tcod.console_put_char(con, object.x, object.y, " ", tcod.BKGND_NONE)

        pass

    def render_map(self):

        for tile_column in self.game.map:
            for tile in tile_column:
                Renderer.draw_tile(self.console, tile, visible = self.game.fov_map.fov[tile.y][tile.x])

    def clear_map(self):

        for tile_column in self.game.map:
            for tile in tile_column:
                Renderer.clear_tile(self.console, tile)

    def draw_tile(con, tile, visible = True):
        if (visible == True):
            # TODO fov code?
            if (not tile.explored == True):
                tile.explored = True

            if (tile.blocking == True):
                # Draw a wall tile
                tcod.console_set_char_background(con, tile.x, tile.y, color_light_wall, tcod.BKGND_SET)
            elif (tile.walkable == True and tile.blocking == False):
                # if not a blocking tile, draw a walkable tile
                tcod.console_set_char_background(con, tile.x, tile.y, color_walkable_tile, tcod.BKGND_SET)
        elif (visible == False):
            if (tile.explored == True):
                if (tile.blocking == True):
                    # Draw a wall tile
                    tcod.console_set_char_background(con, tile.x, tile.y, color_dark_wall, tcod.BKGND_SET)
                elif (tile.walkable == True and tile.blocking == False):
                    # if not a blocking tile, draw a walkable tile
                    tcod.console_set_char_background(con, tile.x, tile.y, color_walkable_dark_tile, tcod.BKGND_SET)

        else:
            # if not any of those, draw an empty tile TODO
            return

    def clear_tile(con, tile):
        tcod.console_set_char_background(con, tile.x, tile.y, (0,0,0), tcod.BKGND_SET)

    def render_dashboards(self):
        for dashboard in self.game.dashboards:
            if (dashboard.visible):
                dashboard.draw(self.console)

    def clear_dashboards(self):
        for dashboard in self.game.dashboards:
            dashboard.clear(self.console)
