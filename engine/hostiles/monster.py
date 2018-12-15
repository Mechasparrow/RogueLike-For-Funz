from ..combat import CombatBehavior

# AI Agent
from agents import MonsterAgent

# GameObject
from engine.gameobjects import GameObject


from .hostile_colors import *

class Monster:

    def __init__(self, monster_name, chr):

        self.monster_name = monster_name
        self.chr = chr

        self.colors_for_difficulty = {
            "basic": monster_basic_color,
            "intermediary": monster_itermediate_color,
            "advanced": monster_advanced
        }

        self.monster_stats = {
            "basic": Monster.stat_dictionary(
                10,
                5,
                4
            ),
            "intermediary": Monster.stat_dictionary(
                15,
                7,
                6
            ),

            "advanced": Monster.stat_dictionary(
                25,
                12,
                9
            )
        }

    def stat_dictionary(health, attack, defense):

        return {
            "health": health,
            "attack": attack,
            "defense": defense
        }

    def add_monster_stats_for_evolution(self,monster_difficulty, stat_dictionary):
        if monster_difficulty in self.monster_stats:
            self[monster_difficulty] = stat_dictionary

    def spawn_instance(self, monster_difficulty, monster_target):

        monster_spec = self.monster_stats[monster_difficulty]

        # Add a monter
        #monster_ai = MonsterAI(attack_target=monster_target)
        monster_combat = CombatBehavior(monster_spec["health"], monster_spec["attack"], monster_spec["defense"])
        monster_object = GameObject(0, 0, self.monster_name, self.chr, color = self.colors_for_difficulty[monster_difficulty])
        monster = MonsterAgent.from_gameobject(monster_object, combat_behavior = monster_combat)
        monster.ai_target = monster_target

        return monster
