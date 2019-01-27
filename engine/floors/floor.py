#
#   floor.py
#   purpose: represents a floor of the game
#   @author Michael Navazhylau
#

from engine.mapping import GameMap
import engine

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
        object_dictionaries = []

        for object in self.objects:
            print (object.__class__.__name__)

            # DEBUG code
            if (object.as_dictionary() == None):
                print ("problem!")
                break

            object_dictionaries.append(object.as_dictionary())

        floor_dict = {
            'width': self.width,
            'height': self.height,
            'objects': object_dictionaries,
            'props': self.props,
            'game_map': self.game_map.as_dictionary()
        }

        return floor_dict

    def from_dictionary(floor_dict, g):
        width = floor_dict['width']
        height = floor_dict['height']

        # FIXME convert to proper objects
        objects = floor_dict['objects']
        print (objects)
        parsed_objects = []
        for obj_dict in objects:
            # TODO parse with appropiate entity class
            print (obj_dict)
            object_class = engine.entities[obj_dict['class']]
            print (object_class)
            parsed_object = object_class.from_dictionary(obj_dict, g)
            print(parsed_object)

            ## DEBUG Breaking code
            if (parsed_object == None):
                print ("FAIL")
                break

            parsed_objects.append(parsed_object)

        print ("ALL GOOD")

        props = floor_dict['props']
        game_map = floor_dict['game_map']

        return Floor(width, height, objects = parsed_objects, fov = game_map['fov'], floor_init = None, game = g)

    def empty_objects(self):
        self.objects = []
