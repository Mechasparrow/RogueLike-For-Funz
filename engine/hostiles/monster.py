from ..fighter import Fighter
from ..gameobject import GameObject

# Code to expand relative imports
import sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

from ..ai.ai_monster import MonsterAI
from ..fighter import Fighter
from ..gameobject import GameObject


from gameconstants import monster_basic_color, monster_itermediate_color, monster_advanced

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
        monster_ai = MonsterAI(attack_target=monster_target)
        monster_fighter = Fighter(monster_spec["health"], monster_spec["attack"], monster_spec["defense"], ai = monster_ai)
        monster = GameObject(0, 0, self.monster_name, self.chr, color = self.colors_for_difficulty[monster_difficulty], fighter = monster_fighter)

        return monster
