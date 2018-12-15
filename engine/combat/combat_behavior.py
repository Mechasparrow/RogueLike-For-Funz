from .combat_stats import CombatStats

class CombatBehavior:

    def __init__(self, combat_stats = None, fighter_name = None):

        if (fighter_name):
            self.fighter_name = fighter_name
        else:
            self.fighter_name = "unspecified"

        self.combat_stats = combat_stats

        if (self.combat_stats):
            self.current_health = self.combat_stats.max_health
        else:
            self.current_health = 0

        self.current_xp = 0

        self.dead = False

    def create_combat_behavior_manual(max_health, attack, defense, xp_drop = None, level = None, fighter_name = None):
        combat_behavior = CombatBehavior(combat_stats = CombatStats(max_health, attack, defense, xp_drop, level), fighter_name = fighter_name)
        return combat_behavior

    def get_combat_stats(self):
        return self.combat_stats

    def die(self):
        print (self.fighter_name + " was killed")
        if (self.combat_stats.xp_drop):
            print (self.fighter_name + " dropped " + str(self.combat_stats.xp_drop) + " xp")

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

    def gain_xp(self, xp):
        self.current_xp = self.current_xp + xp
        print (self.fighter_name + " has gained " + str(xp) + " xp")

    def gain_health(self, health):
        self.current_health = self.current_health + health
        if (self.current_health > self.combat_stats.max_health):
            self.current_health = self.combat_stats.max_health

        print (self.fighter_name + " has gained " + str(health) + " health")
