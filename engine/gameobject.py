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

    def anticipate_move(self, dx, dy):
        potential_x = self.x + dx
        potential_y = self.y + dy

        return (potential_x, potential_y)

    def move(self, dx, dy):

        game_map = self.game.map

        if (game_map):
            anticipated_move = self.anticipate_move(dx, dy)

            tile = game_map.tiles[anticipated_move[0]][anticipated_move[1]]

            if (tile.blocking == True or tile.walkable == False):
                return
            else:
                self.x = anticipated_move[0]
                self.y = anticipated_move[1]
        else:
            self.x += dx
            self.y += dy
