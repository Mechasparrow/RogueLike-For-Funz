#
#   floor.py
#   purpose: represents a floor of the game
#   @author Michael Navazhylau
#

from engine.mapping import GameMap

class Floor:

    def __init__(self, width, height, objects = None, fov = True, floor_init = None, game = None):
        self.game = game
        self.width = width
        self.height = height
        self.objects = objects
        self.props = {}
        self.game_map = GameMap(self.width, self.height, fov = fov)

        # Initialize the floor DEBUG
        if (floor_init):
            floor_init(self)

    def empty_objects(self):
        self.objects = []