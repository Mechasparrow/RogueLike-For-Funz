# Purpose: Monster model for monster class of different types
# i.e Goblins, Serpents
# monster.py
# Author: Michael Navazhylau

# polyfill
import sys
sys.path.append("..")

# import combat
from engine.combat import CombatBehavior, CombatStats, LevelingSystem

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

    def __init__(self, monster_name, chr, leveling_deltas = None):

        self.monster_name = monster_name
        self.chr = chr
        # Leveling Deltas
        if (leveling_deltas == None):
            self.leveling_deltas = LevelingSystem.generate_update_stats_deltas(0,0,0,0)
        else:
            self.leveling_deltas = leveling_deltas

        # difficulty colors
        self.colors_for_difficulty = {
            "basic": monster_basic_color,
            "intermediary": monster_itermediate_color,
            "advanced": monster_advanced
        }

        # generate basic stats for different levels
        self.base_monster_stats = CombatStats(
            10,
            5,
            4,
            xp_drop = 10
        )

    # spawn a specific version of the monster of specified difficulty
    def spawn_instance(self, level, monster_target):

        monster_spec = self.base_monster_stats

        # Add a monter
        #monster_ai = MonsterAI(attack_target=monster_target)
        monster_combat = CombatBehavior(combat_stats = monster_spec, leveling_system = LevelingSystem(level = level, update_stat_deltas = self.leveling_deltas))

        # Force level up
        if (level):
            for i in range(0, level):
                monster_combat.leveling_system.update_combat_stats_by_delta(monster_combat)
        #

        # label with difficulty level #TODO make configurable
        if (level < 3):
            difficulty = "basic"
        elif (level >= 3 and level < 6):
            difficulty = "intermediary"
        else:
            difficulty = "advanced"

        monster_object = GameObject(0, 0, self.monster_name, self.chr, color = self.colors_for_difficulty[difficulty])
        MonsterAgent = grab_agent()
        monster = MonsterAgent.from_gameobject(monster_object, combat_behavior = monster_combat)
        monster.ai_target = monster_target

        return monster
