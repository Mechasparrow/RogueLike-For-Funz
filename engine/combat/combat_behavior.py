from .combat_stats import CombatStats

class CombatBehavior:

    def __init__(self, max_health, attack, defense, fighter_name = None):

        if (fighter_name):
            self.fighter_name = fighter_name
        else:
            self.fighter_name = "unspecified"

        self.combat_stats = CombatStats(max_health, attack, defense)
        self.current_health = self.combat_stats.max_health
        self.dead = False

    def get_combat_stats(self):
        return self.combat_stats

    def die(self):
        print (self.fighter_name + " was killed")
        self.dead = True

    def attack(self, target):
        print (self.fighter_name + " attacked " + target.fighter_name)
        target.recieve_hit(self.combat_stats.attack)

    def recieve_hit(self, damage):

        print (self.fighter_name + " was hit")

        if ((damage - self.combat_stats.defense) < 0):
            print ("The attack was ineffective")
        else:
            self.current_health = self.current_health - (damage - self.combat_stats.defense)

        if (self.current_health <= 0):
            self.die()
