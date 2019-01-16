# Purpose: Special Floor Manager with dungeons
# dungeon_floor_manager.py
# Author: Michael Navazhylau

from .floor_manager import FloorManager

from engine.mapping import Dungeon, DungeonSpawnStats
from engine.game import *

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
            "dungeon_spawn_stats": self.dungeon_spawn_stats.as_dictionary()
        }

        merged_dict = {**original_dict, **dungeon_floor_dict}
        return merged_dict

    def from_dictionary():

        pass

    def replace_main_entity(self,new_entity):

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

        if (self.main_entity != None):
            add_gameobject_to_floor(new_floor, self.main_entity)

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
