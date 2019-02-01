# Purpose: Model/Class for Dungeon Spawn rates
# dungeon_spawn_stats.py
# Author: Michael Navazhylau

class DungeonSpawnStats:

    def __init__(self, monsters_per_room = None, health_chance = None, stairs_chance = None, upward_stairs_chance = None, chest_spawn_chance = None):
        '''
        Stats regarding spawning of objects in dungeons
        monsters per room
        chance of health drop
        chance of stairs
        chance of upward stairs
        chance of chest spawn
        '''

        # Number of monsters per room
        if (monsters_per_room is None):
            self.monsters_per_room = 0
        else:
            self.monsters_per_room = monsters_per_room

        # Health Chance
        if (health_chance is None):
            self.health_chance = 0
        else:
            self.health_chance = health_chance

        # Regular Stairs Chance
        if (stairs_chance is None):
            self.stairs_chance = 0
        else:
            self.stairs_chance = stairs_chance

        # Upward Stairs Chance
        if (upward_stairs_chance is None):
            self.upward_stairs_chance = 0
        else:
            self.upward_stairs_chance = upward_stairs_chance

        # Chest Spawn Chance
        if (chest_spawn_chance is None):
            self.chest_spawn_chance = 0
        else:
            self.chest_spawn_chance = chest_spawn_chance

    def as_dictionary(self):
        stats_dictionary = {
            'monsters_per_room': self.monsters_per_room,
            'health_chance': self.health_chance,
            'stairs_chance': self.stairs_chance,
            'upward_stairs_chance': self.upward_stairs_chance,
            'chest_spawn_chance': self.chest_spawn_chance
        }

        return stats_dictionary

    def from_dictionary(dictionary, g):
        return DungeonSpawnStats(monsters_per_room = dictionary['monsters_per_room'], health_chance = dictionary['health_chance'], stairs_chance = dictionary['stairs_chance'], upward_stairs_chance = dictionary['upward_stairs_chance'], chest_spawn_chance = dictionary['chest_spawn_chance'])
