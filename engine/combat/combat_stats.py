# combat_stats.py
# Provide combat stats of a combatant
# Author: Michael Navazhylau

class CombatStats:
    # params: Maximum Health, Attack ability, Defense ability, optional xp dropped when killed, level of combatant
    def __init__(self, max_health, attack, defense, xp_drop = 0):
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.xp_drop = xp_drop

    def as_dictionary(self):
        return {
            'max_health': self.max_health,
            'attack': self.attack,
            'defense': self.defense,
            'xp_drop': self.xp_drop
        }

    def from_dictionary():

        pass
