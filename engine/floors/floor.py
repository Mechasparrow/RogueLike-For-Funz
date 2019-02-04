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

    def repair_monster_agents(objects):
        parsed_objects = objects
        for parsed_object in parsed_objects:
            object_name = parsed_object.__class__.__name__
            if (object_name == 'MonsterAgent'):
                ai_target = parsed_object.ai_target
                existing_ai_targets = list(filter(lambda object: object.name == ai_target.name, parsed_objects))
                if len(existing_ai_targets) > 0:
                    parsed_object.ai_target = existing_ai_targets[0]

        return parsed_objects

    def from_dictionary(floor_dict, g):
        width = floor_dict['width']
        height = floor_dict['height']

        # Converts all objects to proper objects
        objects = floor_dict['objects']
        parsed_objects = []
        for obj_dict in objects:
            object_class = engine.entities[obj_dict['class']]
            parsed_object = object_class.from_dictionary(obj_dict, g)

            ## DEBUG Breaking code
            if (parsed_object == None):
                print ("FAIL")
                break

            parsed_objects.append(parsed_object)

        # NOTE inefficient
        parsed_objects = Floor.repair_monster_agents(parsed_objects)

        props = floor_dict['props']

        # FIXME convert to proper game map
        game_map = GameMap.from_dictionary(floor_dict['game_map'], g)

        floor = Floor(width, height, objects = parsed_objects, fov = game_map.fov, floor_init = None, game = g)
        floor.game_map = game_map
        floor.props = props
        return floor

    def empty_objects(self):
        self.objects = []
