import tcod

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
                if (self.game.fov_map.fov[tile.y][tile.x] == True):
                    tile.draw(self.console, visible = True)
                else:
                    tile.draw(self.console, visible = False)

    def clear_map(self):

        for tile_column in self.game.map:
            for tile in tile_column:
                tile.clear(self.console)

    def render_dashboards(self):
        for dashboard in self.game.dashboards:
            if (dashboard.visible):
                dashboard.draw(self.console)

    def clear_dashboards(self):
        for dashboard in self.game.dashboards:
            dashboard.clear(self.console)
