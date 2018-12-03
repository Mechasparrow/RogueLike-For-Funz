from .rect import Rect
from .room import Room

class Dungeon:

    def __init__(self, map, rooms = []):
        self.map = map
        self.rooms = rooms

    def add_room(self, room):
        self.rooms.append(room)

    def add_room_by_position_and_width(self, x, y, w, h):
        new_rect = Rect(x,y,w,h)
        new_room = Room(self.map, new_rect)
        self.add_room(new_room)

    def add_room_by_rect(self, rect):
        new_room = Room(self.map, rect)
        self.add_room(new_room)

    def push_dungeon_to_map(self):
        for room in self.rooms:
            room.draw_room()
