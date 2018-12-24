#
#   floor.py
#   purpose: represents a floor of the game
#   @author Michael Navazhylau
#

from engine.mapping import GameMap

class Floor:

    def __init__(self, width, height, objects = [], fov = True):
        self.width = width
        self.height = height
        self.objects = objects
        self.game_map = GameMap(self.width, self.height, fov = fov)
