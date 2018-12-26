# Purpose: Dashboard Model for Displaying Combat information about an entity
# combat_dashboard.py
# Author: Michael Navazhylau

# import lib
import tcod

# Extends from DashboardBase
from .dashboard import DashboardBase

class CombatDashboard(DashboardBase):

    # Same params as DashboardBase
    # with additional parameter of combat behavior to render information
    def __init__(self, x, y, width, height, combat_behavior, visible = True):
        DashboardBase.__init__(self, x, y, width, height, visible, dashboard_type = "combat")
        self.combat_behavior = combat_behavior

    # Render stats to the dash console
    def render_stats_to_console(self):
        health = self.combat_behavior.current_health
        defense = self.combat_behavior.combat_stats.defense
        damage = self.combat_behavior.combat_stats.attack
        current_xp = self.combat_behavior.current_xp
        current_level = self.combat_behavior.leveling_system.level

        health_string = "Health: " + str(health)
        defense_string = "Defense: " + str(defense)
        damage_string = "Damage: " + str(damage)
        level_string = "Level: " + str(current_level)
        xp_string = "XP: " + str(current_xp)

        self.dash_console.print_(0,0, health_string)
        self.dash_console.print_(0,1, defense_string)
        self.dash_console.print_(0,2, damage_string)
        self.dash_console.print_(0,3, level_string)
        self.dash_console.print_(0,4, xp_string)

    # update the dash console with combat information
    def update_dash_console(self):
        self.render_stats_to_console()
        pass
