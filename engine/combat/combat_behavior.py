# CombatBehaviror provides the core for combat in the roguelike
# combat_behavior.py
# Author: Michael Navazhylau

# import libs
from .combat_stats import CombatStats

# CombastBehavior model
class CombatBehavior:

    # initialization
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

        # initially the combatant is not dead
        self.dead = False

    # TODO create more appropiate name
    # creates the combat behavior with combat stats manually supplied
    def create_combat_behavior_manual(max_health, attack, defense, xp_drop = None, level = None, fighter_name = None):
        combat_behavior = CombatBehavior(combat_stats = CombatStats(max_health, attack, defense, xp_drop, level), fighter_name = fighter_name)
        return combat_behavior

    # get the combat stats (Max_Health, Defense, etc)
    def get_combat_stats(self):
        return self.combat_stats

    # updates the combatants death status
    def die(self):
        print (self.fighter_name + " was killed")
        if (self.combat_stats.xp_drop):
            print (self.fighter_name + " dropped " + str(self.combat_stats.xp_drop) + " xp")

        self.dead = True

    # attack another combatant
    def attack(self, target):
        print (self.fighter_name + " attacked " + target.fighter_name)
        target.recieve_hit(self.combat_stats.attack)

    # recieve a damage
    def recieve_hit(self, damage):

        print (self.fighter_name + " was hit")

        if ((damage - self.combat_stats.defense) < 0):
            print ("The attack was ineffective")
        else:
            self.current_health = self.current_health - (damage - self.combat_stats.defense)

        if (self.current_health <= 0):
            self.die()

    # gain xp
    def gain_xp(self, xp):
        self.current_xp = self.current_xp + xp
        print (self.fighter_name + " has gained " + str(xp) + " xp")

    # gain health
    def gain_health(self, health):
        self.current_health = self.current_health + health
        if (self.current_health > self.combat_stats.max_health):
            self.current_health = self.combat_stats.max_health

        print (self.fighter_name + " has gained " + str(health) + " health")
