# Purpose: Model/Class for Dungeon generation
# dungeon.py
# Author: Michael Navazhylau

# import libs
import tcod
import random

# import dungeon utils
from .rect import Rect
from .room import Room
from .tunnel import Tunnel
from .stairs import Stairs
from .chest import Chest

# polyfill
import sys
sys.path.append("..")

# Engine imports
from engine.gameobjects import GameObject
from engine.items import Item
from engine.hostiles import *
from engine.game import *
from engine.pickups import *

# Monsters to spawn
from .monsters import monsters

#Spawn stats
from .dungeon_spawn_stats import DungeonSpawnStats

class Dungeon:

    # params
    # ref to game
    # ref to map
    # list of rooms for dungeon
    # function for generating next floor
    def __init__(self, floor, rooms = [], dungeon_spawn_rates = None, generate_floor = None, go_upward = None, game = None):
        self.game = game
        self.floor = floor
        self.map = self.floor.game_map
        self.rooms = rooms
        self.generate_floor = generate_floor
        self.go_upward = go_upward

        if (dungeon_spawn_rates is None):
            self.dungeon_spawn_rates = DungeonSpawnStats()
        else:
            self.dungeon_spawn_rates = dungeon_spawn_rates

        self.gen_dungeon()

    def gen_dungeon(self):

        # Clear the map DEAD to us
        self.rooms = []
        self.map.clear_tiles()

        # generate dungeon bsp
        map_width =  self.map.width
        map_height = self.map.height

        bsp = tcod.bsp.BSP(x=0,y=0, width = map_width-1, height = map_height-1)
        bsp.split_recursive(
            depth=4,
            min_width=9,
            min_height=9,
            max_horizontal_ratio=1.25,
            max_vertical_ratio=1.25
        )
        self.traverse_bsp(bsp)

    # traverse the dungeon bsp
    def traverse_bsp(self, node):

        for child in node.children:
            self.traverse_bsp(child)

        if node.children:
            self.bsp_connect_rooms(node)
        else:
            self.bsp_create_room(node)

    # connect bsp dungeon rooms
    def bsp_connect_rooms(self, node):
        (node1, node2) = node.children
        room1 = self.bsp_find_node_room(node1)
        room2 = self.bsp_find_node_room(node2)
        self.connect_rooms(room1, room2)

    # create a room for the bsp
    def bsp_create_room(self, node):
        padding = 5
        node_rect = Rect(node.x+padding, node.y+padding, node.width-padding, node.height-padding)

        new_room = Room(self.map.tiles, node_rect)
        self.add_room(new_room)

    # find a specific room in a bsp node tree
    def bsp_find_node_room(self, node):

        for room in self.rooms:
            room_centre = room.rect.center()
            if (node.contains(room_centre[0], room_centre[1])):
                return room

    # add a room to a dungeon
    def add_room(self, room):
        self.rooms.append(room)

    # connect 2 rooms together by tunnel
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


            room_a_x = tcod.random_get_int(0,(room_a.left_edge() + 1), room_a.right_edge()) - 1
            room_b_x = tcod.random_get_int(0,(room_b.left_edge() + 1), room_b.right_edge()) - 1

            if (room_a.top_edge() < room_b.bottom_edge()):
                tunnel_point1 = (room_a_x, room_a.bottom_edge())
                tunnel_point2 = (room_b_x, room_b.top_edge())

            else:
                tunnel_point2 = (room_a_x, room_a.top_edge())
                tunnel_point1 = (room_b_x, room_b.bottom_edge())


            vert_tunnel = Tunnel(tunnel_point1, tunnel_point2, "v")
            vert_tunnel.draw_tunnel(self.map.tiles)

        else:
            # Already connected
            return

    # add a room to the dungeon at a specific position
    def add_room_by_position_and_width(self, x, y, w, h):
        new_rect = Rect(x,y,w,h)
        new_room = Room(self.map.tiles, new_rect)
        self.add_room(new_room)

    # add a room by a rectangle
    def add_room_by_rect(self, rect):
        new_room = Room(self.map.tiles, rect)
        self.add_room(new_room)

    # grab a random room from the list of rooms
    def grab_random_room(self):
        random_room = random.choice(self.rooms)
        return random_room

    # add monsters to all the rooms
    def add_monsters_to_rooms(self, monster_target, monster_cnt):

        for room in self.rooms:
            self.add_monsters_to_room(room, monster_target, monster_cnt)

    # add health pickups to the rooms with a specified chance
    def add_health_to_rooms(self, chance):
        for room in self.rooms:
            chnce = tcod.random_get_int(0, 0, 100)
            if (chnce <= (chance * 100)):
                self.add_health_to_room(room)

    # add health drop to a specific room
    def add_health_to_room(self, room):

        rando_x = tcod.random_get_int(0, room.rect.x, room.rect.x + room.rect.w - 1)
        rando_y = tcod.random_get_int(0, room.rect.y, room.rect.y + room.rect.h - 1)

        # Add health pickup

        pickup = HealthDrop(rando_x, rando_y, 10, game = self.game)

        #Only spawn a health drop on a tile that does not have anything else on it
        if not (gameobjects_exist_at_point(self.floor, rando_x, rando_y)):
            add_gameobject_to_floor(self.floor, pickup)

    # add chests to the rooms with a specified chance
    def add_chests_to_rooms(self, chance):
        for room in self.rooms:
            chnce = tcod.random_get_int(0, 0, 100)
            if (chnce <= (chance * 100)):
                self.add_chest_to_room(room)

    # add chest to a specific room
    def add_chest_to_room(self, room):

        rando_x = tcod.random_get_int(0, room.rect.x, room.rect.x + room.rect.w - 1)
        rando_y = tcod.random_get_int(0, room.rect.y, room.rect.y + room.rect.h - 1)

        # DEBUG give it a dummy item
        dummy_item = Item("trash item")

        # Add the chest
        # Only adds chest to game if it is on a tile that does not have another object on it
        chest = Chest(rando_x, rando_y, game = self.game, chest_item = dummy_item)

        if not (gameobjects_exist_at_point(self.floor, rando_x, rando_y)):
            add_gameobject_to_floor(self.floor, chest)


    # add monsters to a room
    def add_monsters_to_room(self, room, monster_target, monster_cnt):

        for i in range(0, monster_cnt):
            rando_x = tcod.random_get_int(0, room.rect.x, room.rect.x + room.rect.w - 1)
            rando_y = tcod.random_get_int(0, room.rect.y, room.rect.y + room.rect.h - 1)

            # Add a monter
            monster_values = list(monsters.values())
            rando_monster_blueprint = monster_values[tcod.random_get_int(0, 0, len(monster_values) - 1)]

            # OBSOLETE
            #rando_difficulty = ["basic", "intermediary", "advanced"][tcod.random_get_int(0,0,2)]

            monster = rando_monster_blueprint.spawn_instance(self.game.floor_manager.current_floor_number, monster_target)
            monster.game = self.game
            monster.combat_behavior.game = self.game
            monster.x = rando_x
            monster.y = rando_y

            # Only adds monster to game if it is not on a tile that has something else on it
            if not (gameobjects_exist_at_point(self.floor, rando_x, rando_y)):
                add_agent_to_floor(self.floor, monster)
                print ("spawned!")


    # add stairs to a random room
    def add_stairs_to_dungeon(self, chance, one_room = False, upward = False):

        for i in self.rooms:
            chnce = tcod.random_get_int(0, 0, 100)

            if (chnce <= (chance * 100)):
                random_room = self.grab_random_room()
                (room_centre_x, room_centre_y) = random_room.rect.center()

                stairs = Stairs(room_centre_x, room_centre_y, name = "dungeon_stairs", game = self.game, stairs_behavior = self.generate_floor)

                # Upward version of stairs
                if (upward):
                    stairs.color = (255, 153, 204)
                    stairs.stairs_behavior = self.go_upward

                    # If first floor don't create any upward stairs
                    if (self.game.floor_manager.current_floor_number <= 1):
                        return

                # place stair at room center if no other object is there
                if not (gameobjects_exist_at_point(self.floor, room_centre_x, room_centre_y)):
                    add_gameobject_to_floor(self.floor, stairs)

    def add_spawns_to_dungeon(self, monster_target = None):

        if (monster_target != None):
            self.add_monsters_to_rooms(monster_target, monster_cnt = self.dungeon_spawn_rates.monsters_per_room)

        self.add_health_to_rooms(self.dungeon_spawn_rates.health_chance)
        self.add_stairs_to_dungeon(self.dungeon_spawn_rates.stairs_chance)
        self.add_stairs_to_dungeon(self.dungeon_spawn_rates.upward_stairs_chance, upward = True)
        self.add_chests_to_rooms(self.dungeon_spawn_rates.chest_spawn_chance)


    # push the dungeon to the game map
    def push_dungeon_to_map(self):

        for room in self.rooms:
            room.draw_room()

        self.map.update_fov_map()
