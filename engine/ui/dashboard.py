import tcod

class DashboardBase:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.dash_console = tcod.console.Console(self.width, self.height)

    def draw(self, console_out):
        tcod.console_blit(self.dash_console, 0, 0, self.width, self.height, console_out, self.x, self.y)

    def clear(self, console_out):
        self.dash_console.clear()
        self.draw(console_out)
