# Purpose: Provides a core fundamental unit of representing objects in the game world
# gameobject.py
# Author: Michael Navazhylau

# Import libs
import tcod

class GameObject:

    # params
    # position, name, character, a color, reference to game world, gameobject type
    def __init__(self, x, y, name, chr, color, game = None, type = "Base"):
        self.x = x
        self.y = y
        self.name = name
        self.chr = chr
        self.color = color
        self.game = game
        self.type = type

    def as_dictionary(self):
        return {
            'x': self.x,
            'y': self.y,
            'name': self.name,
            'chr': self.chr,
            'color': self.color,
            'type': self.type
        }

    def from_dictionary():

        pass

    # return a point at the generated from anticipating a move with a dx, dy
    def anticipate_move(self, dx, dy):
        potential_x = self.x + dx
        potential_y = self.y + dy

        return (potential_x, potential_y)

    # move gameobject a certain dx, dy
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
