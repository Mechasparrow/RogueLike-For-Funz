# LevelingSystem provides the core for leveling for combat behavior
# leveling_system.py
# Author: Michael Navazhylau

from .combat_stats import CombatStats
from engine.game import *

class LevelingSystem:

    #params
    # level
    # amount of xp required to level up
    # should a level up restore health

    def __init__(self, level = 1, level_up_threshold = 100, restore_health = True, update_stat_deltas = None):
        self.level = level
        self.level_up_threshold = level_up_threshold
        self.restore_health = restore_health

        # Logging behavior
        self.logging_function = None
        self.enable_default_logging()

        if (update_stat_deltas):
            self.update_stat_deltas = update_stat_deltas
        else:
            self.update_stat_deltas = LevelingSystem.generate_update_stats_deltas(0,0,0,0)

    def as_dictionary(self):

        return {
            'level': self.level,
            'level_up_threshold': self.level_up_threshold,
            'restore_health': self.restore_health,
            'update_stat_deltas': self.update_stat_deltas
        }

    def from_dictionary(dictionary, g):
        return LevelingSystem(level = dictionary['level'], level_up_threshold = dictionary['level_up_threshold'], restore_health = dictionary['restore_health'], update_stat_deltas = dictionary['update_stat_deltas'])


    # TODO generalize
    # Enable regular logging
    def enable_default_logging(self):
        def logging_function(message):
            print (message)

        self.logging_function = logging_function

    # Enable dashboard logging
    def enable_dashboard_logging(self, game):
        def dashboard_logging(message):
            push_message_to_log(game, message)

        self.logging_function = dashboard_logging

    def generate_update_stats_deltas(d_max_health, d_attack, d_defense, d_xp_drop = 0):
        return {
            "d_health": d_max_health,
            "d_attack": d_attack,
            "d_defense": d_defense,
            "d_xp_drop": d_xp_drop
        }

    # updates the system to see if a level up is valid
    def update_leveling_system(self, combat_behavior):
        if (combat_behavior.current_xp >= self.level_up_threshold):
            self.level_up(combat_behavior)

    # updates the combat stats of a combat_behavior if valid
    def update_combat_stats_by_delta(self, combat_behavior):
        if (self.update_stat_deltas):
            deltas = self.update_stat_deltas
            old_combat_stats = combat_behavior.combat_stats
            new_combat_stats = CombatStats(max_health = old_combat_stats.max_health + deltas["d_health"], attack = old_combat_stats.attack + deltas["d_attack"], defense = old_combat_stats.defense + deltas["d_defense"], xp_drop = old_combat_stats.xp_drop + deltas["d_xp_drop"])
            combat_behavior.combat_stats = new_combat_stats
            self.logging_function ("combat stats updated!")

    # restores health of combatant if valid option
    def restore_combatant_health(self, combat_behavior):
        if (self.restore_health):
            combat_behavior.current_health = combat_behavior.combat_stats.max_health
            self.logging_function(str(combat_behavior.fighter_name) + " health restored")

    # Levels up the combat behavior entity if able to
    def level_up(self, combat_behavior):
        self.level += 1
        self.logging_function(str(combat_behavior) + " has leveled up!")

        combat_behavior.current_xp = combat_behavior.current_xp - self.level_up_threshold

        if (combat_behavior.combat_stats):

            # Update the modify the combat stats
            self.update_combat_stats_by_delta(combat_behavior)

            # Restore entity health
            self.restore_combatant_health(combat_behavior)
