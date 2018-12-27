# Purpose: Key model for handling game floors
# floor_manager.py
# Author: Michael Navazhylau
# TODO use properties man

from .floor import Floor

from engine.mapping import *

class FloorManager:

    def __init__(self, floor_width, floor_height, floors = None, game = None, custom_floor_gen = None):
        '''
        @params
        floors: list of all the floors on the floor manager
        current_floor: the index of the current active floor
        '''

        self.game = game
        self.floor_width = floor_width
        self.floor_height = floor_height

        if (custom_floor_gen == None):
            self.custom_floor_gen = self.default_custom_floor_gen
        else:
            self.custom_floor_gen = custom_floor_gen

        # If no floors specified, set it to empty
        if floors is None:
            self.floors = []

        self.current_floor_number = 0

    def default_custom_floor_gen(self):
        return self.gen_empty_floor()

    def gen_empty_floor(self):
        '''
        generates an empty floor
        '''

        empty_floor = Floor(self.floor_width, self.floor_height, objects = [], game = self.game)
        return empty_floor

    def gen_floor(self):
        '''
        generates a regular floor with custom parameters
        '''
        return self.custom_floor_gen()

    # TODO IDK ???
    def remove_floor(self, floor):
        raise NotImplementedError

    def add_floor(self, floor):
        '''
        Adds a floor to the manager
        '''
        self.floors.append(floor)

    def add_empty_floor(self):
        '''
        Adds an emtpy floor to the floor FloorManager
        '''

        self.add_floor(self.gen_empty_floor())

    def goto_next_floor(self, callback = None):
        '''
        Goes to the next floor
        and runs any additional code (callback)
        '''

        #if (self.current_floor_number )

        self.current_floor_number += 1


        # If callback exists, run it
        if (callback):
            callback()

    def goto_previous_floor(self, callback = None):
        '''
        Goes to the previous floor
        and runs any additional code (callback)
        '''

        self.current_floor_number -= 1

        # If callback exists, run it
        if (callback):
            callback()

    def get_current_floor(self):
        '''
        Gets the current active floor
        '''

        if (self.current_floor_number):
            return self.floors[self.current_floor_number - 1]
        else:
            return None

    def get_floor_count(self):
        '''
        returns the amount of floors so far
        '''

        return len(self.floors)

    # TODO shift floor gen over here... (dungeon)
