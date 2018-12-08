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

    def draw(self, console_out):
        tcod.console_blit(self.dash_console, 0, 0, self.width, self.height, console_out, self.x, self.y)

    def clear(self, console_out):
        self.dash_console.clear()
        tcod.console_blit(self.dash_console, 0, 0, self.width, self.height, console_out, self.x, self.y)
