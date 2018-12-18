# Purpose: Monster model for monster class of different types
# i.e Goblins, Serpents
# monster.py
# Author: Michael Navazhylau

# polyfill
import sys
sys.path.append("..")

# import combat
from engine.combat import CombatBehavior, CombatStats

# import agent when needed
def grab_agent():
    from engine.agents import MonsterAgent
    return MonsterAgent

# GameObject
from engine.gameobjects import GameObject

# constants
from .hostile_colors import *

class Monster:

    # params
    # name of monster
    # character of monster

    def __init__(self, monster_name, chr):

        self.monster_name = monster_name
        self.chr = chr

        # difficulty colors
        self.colors_for_difficulty = {
            "basic": monster_basic_color,
            "intermediary": monster_itermediate_color,
            "advanced": monster_advanced
        }

        # generate basic stats for different levels
        self.monster_stats = {
            "basic": CombatStats(
                10,
                5,
                4,
                xp_drop = 4
            ),
            "intermediary": CombatStats(
                15,
                7,
                6,
                xp_drop = 6
            ),

            "advanced": CombatStats(
                25,
                12,
                9,
                xp_drop = 10
            )
        }


    # add a monster stat for specific difficulty
    def add_monster_stats_for_evolution(self,monster_difficulty, stat_dictionary):
        if monster_difficulty in self.monster_stats:
            self[monster_difficulty] = stat_dictionary

    # spawn a specific version of the monster of specified difficulty
    def spawn_instance(self, monster_difficulty, monster_target):

        monster_spec = self.monster_stats[monster_difficulty]

        # Add a monter
        #monster_ai = MonsterAI(attack_target=monster_target)
        monster_combat = CombatBehavior(combat_stats = monster_spec)
        monster_object = GameObject(0, 0, self.monster_name, self.chr, color = self.colors_for_difficulty[monster_difficulty])
        MonsterAgent = grab_agent()
        monster = MonsterAgent.from_gameobject(monster_object, combat_behavior = monster_combat)
        monster.ai_target = monster_target

        return monster
