# CombatBehaviror provides the core for combat in the roguelike
# combat_behavior.py
# Author: Michael Navazhylau

# import libs
from .combat_stats import CombatStats
from .leveling_system import LevelingSystem

# Logging system
from engine.game import *

# CombastBehavior model
class CombatBehavior:

    # initialization
    # params
    # combat stats of the combat behavior (max_health, attack, defense, etc)
    # name of fighter
    # current level of combatant through leveling system

    # TODO level up options abstraction
    def __init__(self, combat_stats = None, fighter_name = None, leveling_system = LevelingSystem(), game = None):

        self.game = game

        # Fighter name initialization
        if (fighter_name):
            self.fighter_name = fighter_name
        else:
            self.fighter_name = "unspecified"

        # Combat stats intilization
        self.combat_stats = combat_stats
        if (self.combat_stats):
            self.current_health = self.combat_stats.max_health
        else:
            self.current_health = 0

        # TODO consider shoving into leveling system
        self.current_xp = 0

        # Combat Behavior normally initialized with level 1
        self.leveling_system = leveling_system

        # initially the combatant is not dead
        self.dead = False


    # TODO create more appropiate name
    # creates the combat behavior with combat stats manually supplied
    def create_combat_behavior_manual(max_health, attack, defense, xp_drop = 0, fighter_name = None, leveling_system = LevelingSystem()):
        combat_behavior = CombatBehavior(combat_stats = CombatStats(max_health, attack, defense, xp_drop), fighter_name = fighter_name, leveling_system = leveling_system)
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
        push_message_to_log(self.game, self.fighter_name + " attacked " + target.fighter_name)
        target.recieve_hit(self.combat_stats.attack)

    # recieve a damage
    def recieve_hit(self, damage):

        push_message_to_log(self.game, self.fighter_name + " was hit")

        if ((damage - self.combat_stats.defense) < 0):
            push_message_to_log(self.game,"The attack was ineffective")
        else:
            self.current_health = self.current_health - (damage - self.combat_stats.defense)

        if (self.current_health <= 0):
            self.die()

    # gain xp
    def gain_xp(self, xp):
        self.current_xp = self.current_xp + xp
        push_message_to_log(self.game,self.fighter_name + " has gained " + str(xp) + " xp")

        # leveling system
        if (self.leveling_system):
            self.leveling_system.update_leveling_system(self)

    # gain health
    def gain_health(self, health):
        self.current_health = self.current_health + health
        if (self.current_health > self.combat_stats.max_health):
            self.current_health = self.combat_stats.max_health

        push_message_to_log(self.game, self.fighter_name + " has gained " + str(health) + " health")
