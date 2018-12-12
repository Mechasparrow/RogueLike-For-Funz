import tcod

class DashboardBase:

    def __init__(self, x, y, width, height, visible = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible

        self.dash_console = tcod.console.Console(self.width, self.height)

    def hide_dashboard(self):
        self.visible = False

    def show_dashboard(self):
        self.visible = True

    # Abstract method
    def update_dash_console(self):

        pass
