# Purpose: Renderer system for a game
# renderer.py
# Author: Michael Navazhylau

# import libs
import tcod

# import additional sub-renderers
from .gameobject_renderer import *
from .map_renderer import *
from .dashboard_renderer import *

class Renderer:

    # Takes in ref to game
    def __init__(self, game):

        self.console = game.root_console
        self.game = game

    # Render everything to the root game console
    def render_all(self):
        # Render the dashboards
        render_dashboards(self.console, self.game.dashboards)

        # Render the gameobjects
        render_gameobjects(self.console, self.game.objects, self.game.map.fov_map)

        # Rendering the map
        render_map(self.console, self.game.map)

    # Update the root game console
    def update_console(self):
        tcod.console_flush() # Show the console

    # Clear everything from the root game console
    def clear_all(self):
            #clear dashboards
            clear_dashboards(self.console, self.game.dashboards)

            # clear gameobjects
            clear_gameobjects(self.console, self.game.objects)

            # Clearing the map
            clear_map(self.console, self.game.map)
