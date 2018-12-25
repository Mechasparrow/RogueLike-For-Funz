# Purpose: Model/Class for Dungeon generation
# dungeon.py
# Author: Michael Navazhylau

# polyfill
import sys
sys.path.append("..")

# get the monster class
from engine.hostiles import Monster
from engine.combat import LevelingSystem

# define some monsters
# TODO put in JSON config system
default_leveling_deltas = LevelingSystem.generate_update_stats_deltas(1,1,1,2)

goblin = Monster("Goblin", "G", leveling_deltas = default_leveling_deltas)
druid = Monster("Druid", "D", leveling_deltas = default_leveling_deltas)
serpent = Monster("Serpent", "S", leveling_deltas = default_leveling_deltas)

monsters = {
    "goblin": goblin,
    "druid": druid,
    "serpent": serpent
}
