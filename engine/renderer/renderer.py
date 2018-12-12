import tcod

# import additional renderers
from .gameobject_renderer import *
from .map_renderer import *
from .dashboard_renderer import *

class Renderer:

    def __init__(self, game):

        self.console = game.root_console
        self.game = game

    def render_all(self):
        # Render the dashboards
        render_dashboards(self.console, self.game.dashboards)

        # Render the gameobjects
        render_gameobjects(self.console, self.game.objects, self.game.map.fov_map)

        # Rendering the map
        render_map(self.console, self.game.map)

    def update_console(self):
        tcod.console_flush() # Show the console

    def clear_all(self):
            #clear dashboards
            clear_dashboards(self.console, self.game.dashboards)

            # clear gameobjects
            clear_gameobjects(self.console, self.game.objects)

            # Clearing the map
            clear_map(self.console, self.game.map)
