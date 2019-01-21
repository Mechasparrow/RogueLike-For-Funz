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

    def as_dictionary(self):
        floor_dict = {
            'width': self.width,
            'height': self.height,
            'objects': [object.as_dictionary() for object in self.objects],
            'props': self.props,
            'game_map': self.game_map.as_dictionary()
        }

        return floor_dict

    def from_dictionary(floor_dict, g):
        width = floor_dict['width']
        height = floor_dict['height']

        # FIXME convert to proper objects
        objects = floor_dict['objects']

        props = floor_dict['props']
        game_map = floor_dict['game_map']

        return Floor(width, height, objects = objects, fov = game_map['fov'], floor_init = None, game = g)

    def empty_objects(self):
        self.objects = []
