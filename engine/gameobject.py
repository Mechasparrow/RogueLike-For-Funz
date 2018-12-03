import tcod

class GameObject:

    def __init__(self, x, y, name, chr, color, entity = False, game = None):
        self.x = x
        self.y = y
        self.name = name
        self.chr = chr
        self.color = color
        self.game = game

        # modfiers
        self.entity = entity

    def move(self, dx, dy):

        game_map = self.game.map

        if (self.entity and game_map):
            potential_x = self.x + dx
            potential_y = self.y + dy

            tile = game_map[potential_x][potential_y]

            if (tile.blocking == True or tile.walkable == False):
                return
            else:
                self.x = potential_x
                self.y = potential_y
        else:
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
