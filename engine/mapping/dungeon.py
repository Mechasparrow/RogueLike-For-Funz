import tcod
from .rect import Rect
from .room import Room
from .tunnel import Tunnel
import random

from ..ai.ai_monster import MonsterAI
from ..fighter import Fighter
from ..gameobjects.gameobject import GameObject

from ..hostiles.monster import Monster

from .monsters import monsters

class Dungeon:

    def __init__(self, game, map, rooms = []):
        self.game = game
        self.map = map
        self.rooms = rooms

        # generate bsp
        map_width =  map.width
        map_height = map.height

        self.bsp = tcod.bsp.BSP(x=0,y=0, width = map_width-1, height = map_height-1)
        self.bsp.split_recursive(
            depth=4,
            min_width=9,
            min_height=9,
            max_horizontal_ratio=1.25,
            max_vertical_ratio=1.25
        )
        self.traverse_bsp(self.bsp)

    def traverse_bsp(self, node):

        for child in node.children:
            self.traverse_bsp(child)

        if node.children:
            self.bsp_connect_rooms(node)
        else:
            self.bsp_create_room(node)

    def bsp_connect_rooms(self, node):
        (node1, node2) = node.children
        room1 = self.bsp_find_node_room(node1)
        room2 = self.bsp_find_node_room(node2)
        self.connect_rooms(room1, room2)

    def bsp_create_room(self, node):
        padding = 5
        node_rect = Rect(node.x+padding, node.y+padding, node.width-padding, node.height-padding)
        print (node_rect)
        new_room = Room(self.map.tiles, node_rect)
        self.add_room(new_room)

    def bsp_find_node_room(self, node):

        for room in self.rooms:
            room_centre = room.rect.center()
            if (node.contains(room_centre[0], room_centre[1])):
                return room

        print ("No room was found")
        return

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

            horiz_tunnel.draw_tunnel(self.map.tiles)

            # Horiz tunnel
        elif (room_a.top_edge() < room_b.bottom_edge() or room_b.top_edge() < room_a.bottom_edge()):

            print ("VERT")

            room_a_x = tcod.random_get_int(0,(room_a.left_edge() + 1), room_a.right_edge()) - 1
            room_b_x = tcod.random_get_int(0,(room_b.left_edge() + 1), room_b.right_edge()) - 1

            if (room_a.top_edge() < room_b.bottom_edge()):
                tunnel_point1 = (room_a_x, room_a.bottom_edge())
                tunnel_point2 = (room_b_x, room_b.top_edge())
                print ("a")
            else:
                tunnel_point2 = (room_a_x, room_a.top_edge())
                tunnel_point1 = (room_b_x, room_b.bottom_edge())
                print ("b")

            vert_tunnel = Tunnel(tunnel_point1, tunnel_point2, "v")
            vert_tunnel.draw_tunnel(self.map.tiles)

        else:
            print ("Intersecting")
            # Already connected
            return


    def add_room_by_position_and_width(self, x, y, w, h):
        new_rect = Rect(x,y,w,h)
        new_room = Room(self.map.tiles, new_rect)
        self.add_room(new_room)

    def add_room_by_rect(self, rect):
        new_room = Room(self.map.tiles, rect)
        self.add_room(new_room)

    def grab_random_room(self):
        random_room = random.choice(self.rooms)
        return random_room

    def add_monsters_to_rooms(self, monster_target):

        for room in self.rooms:
            self.add_monsters_to_room(room, monster_target)


    def add_monsters_to_room(self, room, monster_target):
        monster_cnt = 2

        for i in range(0, monster_cnt):
            rando_x = tcod.random_get_int(0, room.rect.x, room.rect.x + room.rect.w - 1)
            rando_y = tcod.random_get_int(0, room.rect.y, room.rect.y + room.rect.h - 1)

            # Add a monter
            monster_values = list(monsters.values())
            rando_monster_blueprint = monster_values[tcod.random_get_int(0, 0, len(monster_values) - 1)]
            rando_difficulty = ["basic", "intermediary", "advanced"][tcod.random_get_int(0,0,2)]

            monster = rando_monster_blueprint.spawn_instance(rando_difficulty, monster_target)
            monster.game = self.game
            monster.x = rando_x
            monster.y = rando_y
            self.game.add_agent_to_game(monster)

    def push_dungeon_to_map(self):
        for room in self.rooms:
            room.draw_room()

        self.game.map.update_fov_map()
