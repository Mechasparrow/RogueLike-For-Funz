import tcod
from .rect import Rect
from .room import Room
from .tunnel import Tunnel


class Dungeon:

    def __init__(self, map, rooms = []):
        self.map = map
        self.rooms = rooms

    def add_room(self, room):
        self.rooms.append(room)

    def connect_rooms(self,room_a, room_b):


        if (room_a.right_edge() < room_b.left_edge() or room_b.right_edge() < room_a.left_edge()):

            room_a_y = tcod.random_get_int(0,(room_a.top_edge() + 1), room_a.bottom_edge()) - 1
            room_b_y = tcod.random_get_int(0,(room_b.top_edge() + 1), room_b.bottom_edge()) - 1



            if (room_a.right_edge() < room_b.left_edge()):
                tunnel_point1 = (room_a.right_edge(),room_a_y)
                tunnel_point2 = (room_b.left_edge(),room_b_y)
            else:
                tunnel_point2 = (room_a.left_edge(),room_a_y)
                tunnel_point1 = (room_b.right_edge(),room_b_y)

            horiz_tunnel = Tunnel(tunnel_point1, tunnel_point2, "h")

            horiz_tunnel.draw_tunnel(self.map)

            # Horiz tunnel
        elif (room_a.top_edge() < room_b.bottom_edge() or room_b.top_edge() < room_a.bottom_edge()):

            print ("VERT")

            room_a_x = room_a.left_edge() + 1
            room_b_x = room_b.right_edge() -3

            if (room_a.top_edge() < room_b.bottom_edge()):
                tunnel_point1 = (room_a_x, room_a.bottom_edge())
                tunnel_point2 = (room_b_x, room_b.top_edge())
                print ("a")
            else:
                tunnel_point2 = (room_a_x, room_a.top_edge())
                tunnel_point1 = (room_b_x, room_b.bottom_edge())
                print ("b")

            vert_tunnel = Tunnel(tunnel_point1, tunnel_point2, "v")
            vert_tunnel.draw_tunnel(self.map)

        else:
            print ("Intersecting")
            # Already connected
            return


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
