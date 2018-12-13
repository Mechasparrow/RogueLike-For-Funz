import tcod

class GameObject:

    def __init__(self, x, y, name, chr, color, game = None, type = "Base"):
        self.x = x
        self.y = y
        self.name = name
        self.chr = chr
        self.color = color
        self.game = game
        self.type = type

    def anticipate_move(self, dx, dy):
        potential_x = self.x + dx
        potential_y = self.y + dy

        return (potential_x, potential_y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
