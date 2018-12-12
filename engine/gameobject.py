import tcod

class GameObject:

    def __init__(self, x, y, name, chr, color, fighter = None, game = None):
        self.x = x
        self.y = y
        self.name = name
        self.chr = chr
        self.color = color
        self.game = game

        # Fighter
        self.fighter = fighter
        if (self.fighter):
            self.fighter.owner = self

    def move(self, dx, dy):

        game_map = self.game.map

        if (self.entity and game_map):
            potential_x = self.x + dx
            potential_y = self.y + dy

            tile = game_map.tiles[potential_x][potential_y]

            if (tile.blocking == True or tile.walkable == False):
                return
            else:
                self.x = potential_x
                self.y = potential_y
        else:
            self.x += dx
            self.y += dy
