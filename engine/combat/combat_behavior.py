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

    def as_dictionary(self):
        return {
            'fighter_name': self.fighter_name,
            'current_health': self.current_health,
            'dead': self.dead,
            'current_xp': self.current_xp,
            'leveling_system': self.leveling_system.as_dictionary(),
            'combat_stats': self.combat_stats.as_dictionary()
        }

    def from_dictionary(dictionary, g):

        if (dictionary == None):
            return None

        parsed_leveling_system= LevelingSystem.from_dictionary(dictionary['leveling_system'], g)
        parsed_combat_stats= CombatStats.from_dictionary(dictionary['combat_stats'], g)

        combat_behavior = CombatBehavior(combat_stats = parsed_combat_stats, fighter_name = dictionary['fighter_name'], leveling_system = parsed_leveling_system, game = g)
        combat_behavior.current_health = dictionary['current_health']
        combat_behavior.dead = dictionary['dead']
        combat_behavior.current_xp = dictionary['current_xp']

        return combat_behavior

    # TODO create more appropiate name
    # creates the combat behavior with combat stats manually supplied
    def create_combat_behavior_manual(max_health, attack, defense, xp_drop = 0, fighter_name = None, leveling_system = LevelingSystem()):
        combat_behavior = CombatBehavior(combat_stats = CombatStats(max_health, attack, defense, xp_drop), fighter_name = fighter_name, leveling_system = leveling_system)
        return combat_behavior

    # updates the combatants death status
    def die(self):
        if (self.combat_stats.xp_drop):
            push_message_to_log(self.game, self.fighter_name + " dropped " + str(self.combat_stats.xp_drop) + " xp")

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
            damage_recieved = (damage - self.combat_stats.defense)
            push_message_to_log(self.game, "Hit with " + str(damage_recieved) + " damage")
            self.current_health = self.current_health - damage_recieved
            push_message_to_log(self.game, str(self.fighter_name) + " now has " + str(self.current_health) + " left")

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
