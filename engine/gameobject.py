import tcod

class GameObject:

    def __init__(self, x, y, chr, color):
        self.x = x
        self.y = y
        self.chr = chr
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, con):
        # Set the color
        tcod.console_set_default_foreground(con, self.color)
        # Draw the object rep on to the console
        tcod.console_put_char(con, self.x, self.y, self.chr, tcod.BKGND_NONE)

    def clear(self, con):
        # Set the color
        tcod.console_set_default_foreground(con, self.color)
        # Draw the object rep on to the console
        tcod.console_put_char(con, self.x, self.y, " ", tcod.BKGND_NONE)
