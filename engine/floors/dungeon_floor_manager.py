# Purpose: Special Floor Manager with dungeons
# dungeon_floor_manager.py
# Author: Michael Navazhylau

from .floor_manager import FloorManager
from .floor import Floor

from engine.mapping import Dungeon, DungeonSpawnStats
from engine.game import *

import engine

class DungeonFloorManager(FloorManager):

    def __init__(self, floor_width, floor_height, floors = None, main_entity = None, dungeon_spawn_stats = None, game = None):
        '''
        Essentially the same params as FloorManager
        '''
        FloorManager.__init__(self, floor_width, floor_height, floors = floors, game = game)

        # entity that permeates between rooms
        # TODO eventually may be more than one
        self.main_entity = main_entity

        # Spawn stats for dungeon, if not specifies, just 0 to all
        if (dungeon_spawn_stats == None):
            self.dungeon_spawn_stats = DungeonSpawnStats()
        else:
            self.dungeon_spawn_stats = dungeon_spawn_stats

    def as_dictionary(self):
        original_dict = super().as_dictionary()

        dungeon_floor_dict = {
            "dungeon_spawn_stats": self.dungeon_spawn_stats.as_dictionary(),
            "main_entity": self.main_entity.as_dictionary()
        }

        merged_dict = {**original_dict, **dungeon_floor_dict}
        return merged_dict

    def from_dictionary(floor_dictionary, g):
        floor_width = floor_dictionary["floor_width"]
        floor_height = floor_dictionary["floor_height"]

        floors = [Floor.from_dictionary(flr_dict, g) for flr_dict in floor_dictionary["floors"]]

        raw_main_entity = floor_dictionary['main_entity']
        main_entity_class = engine.entities[raw_main_entity['class']]
        parsed_main_entity = main_entity_class.from_dictionary(raw_main_entity, g)

        # NOTE TODO reimplement when objectIDs implemented
        for floor in floors:
            for object in floor.objects:
                if (object.name == parsed_main_entity.name):
                    parsed_main_entity = object

        current_floor_number = floor_dictionary["current_floor_number"]

        parsed_dungeon_spawn_stats = DungeonSpawnStats.from_dictionary(floor_dictionary["dungeon_spawn_stats"],g)

        dungeon_floor_manager = DungeonFloorManager(floor_width, floor_height, floors = floors, main_entity = parsed_main_entity, dungeon_spawn_stats = parsed_dungeon_spawn_stats, game = g)
        dungeon_floor_manager.current_floor_number = current_floor_number

        # Save Patches
        for floor in dungeon_floor_manager.floors:
            for object in floor.objects:

                # Patchs stairs so they behave correctly
                if (object.__class__.__name__ == "Stairs"):
                    stair = object

                    downward_behavior = dungeon_floor_manager.generate_and_go_to_next_floor
                    upward_behavior = dungeon_floor_manager.go_floor_up

                    # repairs the stairs so they go in the proper direction
                    if (stair.stairs_direction == "down"):
                        stair.stairs_behavior = downward_behavior
                    elif (stair.stairs_direction == "up"):
                        stair.stairs_behavior = upward_behavior

                    print (stair.stairs_behavior)

                # NOTE may not work if there are custom monster agents.Patches monster agents so they can follow the main character correctly since he propagates throughout floors
                elif (object.__class__.__name__ == "MonsterAgent"):
                    ai_target = object.ai_target
                    if (ai_target.name == parsed_main_entity.name):
                        object.ai_target = parsed_main_entity

        return dungeon_floor_manager


    def replace_main_entity(self, new_entity):

        remove_gameobject_from_floor(self.get_current_floor(), self.main_entity)
        add_gameobject_to_floor(self.get_current_floor(), new_entity);


    def go_floor_up(self):
        self.goto_previous_floor(callback = self.next_floor_when_it_exists)

    def next_floor_when_it_exists(self, current_floor, previous_floor):
        if (self.main_entity != None):
            # remove main_entity from previous floor and set up past location
            previous_floor.props["past_main_x"] = self.main_entity.x
            previous_floor.props["past_main_y"] = self.main_entity.y
            remove_gameobject_from_floor(previous_floor, self.main_entity)

            # add main_entity to current floor at past location
            add_gameobject_to_floor(current_floor, self.main_entity)
            self.main_entity.x = current_floor.props["past_main_x"]
            self.main_entity.y = current_floor.props["past_main_y"]

    def next_floor_when_generated(self,current_floor, previous_floor):
        # remove main_entity from previous floor and set up past location
        # Edge case if there is no previous floor
        if (self.main_entity != None):

            if (previous_floor):
                previous_floor.props["past_main_x"] = self.main_entity.x
                previous_floor.props["past_main_y"] = self.main_entity.y
                print (previous_floor.objects)
                print (self.main_entity)
                previous_floor.objects.remove(self.main_entity)

            # Add main_entity to current floor
            add_gameobject_to_floor(current_floor, self.main_entity)

    def generate_and_go_to_next_floor(self):

        went_to_next_floor = self.goto_next_floor(callback = self.next_floor_when_it_exists)

        if (went_to_next_floor != None):
            return

        new_floor = self.gen_dungeon_floor()
        self.add_floor(new_floor)
        self.goto_next_floor(callback = self.next_floor_when_generated)

    def gen_dungeon_floor(self):

        new_floor = self.gen_empty_floor()

        # NOTE STAIRS
        # Stairs downward generate_and_go_to_next_floor
        # Stairs upward go_floor_up

        dungeon = Dungeon(floor = new_floor, dungeon_spawn_rates = self.dungeon_spawn_stats, generate_floor = self.generate_and_go_to_next_floor, go_upward = self.go_floor_up, game = self.game)
        dungeon.push_dungeon_to_map()

        if (self.main_entity != None):
            # grab random room to spawn in TODO make into dungeon function
            random_dungeon_room = dungeon.grab_random_room()
            (room_centre_x, room_centre_y) = random_dungeon_room.rect.center()

            # Put Player in random dungeon room
            self.main_entity.x = room_centre_x
            self.main_entity.y = room_centre_y


        # Add objects to dungeon
        dungeon.add_spawns_to_dungeon(monster_target = self.main_entity)

        return new_floor
