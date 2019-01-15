# Purpose: Key model for handling game floors
# floor_manager.py
# Author: Michael Navazhylau
# TODO use properties man

from .floor import Floor

from engine.mapping import *

class FloorManager:

    def __init__(self, floor_width, floor_height, floors = None, game = None):
        '''
        @params
        floors: list of all the floors on the floor manager
        current_floor: the index of the current active floor
        '''

        self.game = game
        self.floor_width = floor_width
        self.floor_height = floor_height

        # If no floors specified, set it to empty
        if floors is None:
            self.floors = []
        else:
            self.floors = floors

        self.current_floor_number = 0

    def as_dictionary(self):
        # TODO convert floors list to dictionary as well
        floor_dictionary = {
            "floor_width": self.floor_width,
            "floor_height": self.floor_height,
            "current_floor_number": self.current_floor_number,
            "floors": self.floors
        }

        return floor_dictionary

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
        callback must have a current floor and previous floor parameter
        '''

        # if we are on the last floor then there is no next floor to go to
        if (len(self.floors) == self.current_floor_number):
            return None

        previous_floor = self.get_current_floor()
        self.current_floor_number += 1
        current_floor = self.get_current_floor()

        # If callback exists, run it
        if (callback):
            callback(current_floor, previous_floor)

    def goto_previous_floor(self, callback = None):
        '''
        Goes to the previous floor
        and runs any additional code (callback)
        callback must have a current floor and previous floor parameter
        '''

        # If we are on the last floor, there is no previous floor to go to
        if (self.current_floor_number <= 1):
            return None

        previous_floor = self.get_current_floor()
        self.current_floor_number -= 1
        current_floor = self.get_current_floor()

        # If callback exists, run it
        if (callback):
            callback(current_floor, previous_floor)

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
