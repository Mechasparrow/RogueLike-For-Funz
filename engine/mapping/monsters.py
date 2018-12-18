# Purpose: Model/Class for Dungeon generation
# dungeon.py
# Author: Michael Navazhylau

# polyfill
import sys
sys.path.append("..")

# get the monster class
from engine.hostiles import Monster

# define some monsters
# TODO put in JSON config system
goblin = Monster("Goblin", "G")
druid = Monster("Druid", "D")
serpent = Monster("Serpent", "S")

monsters = {
    "goblin": goblin,
    "druid": druid,
    "serpent": serpent
}
