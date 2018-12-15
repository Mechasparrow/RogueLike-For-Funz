import tcod

from .dashboard import DashboardBase

class CombatDashboard(DashboardBase):

    def __init__(self, x, y, width, height, combat_behavior, visible = True):
        DashboardBase.__init__(self, x, y, width, height, visible)
        self.combat_behavior = combat_behavior

    def render_stats_to_console(self):
        health = self.combat_behavior.current_health
        defense = self.combat_behavior.get_combat_stats().defense
        damage = self.combat_behavior.get_combat_stats().defense
        current_xp = self.combat_behavior.current_xp

        health_string = "Health: " + str(health)
        defense_string = "Defense: " + str(defense)
        damage_string = "Damage: " + str(damage)
        xp_string = "XP: " + str(current_xp)

        self.dash_console.print_(0,0, health_string)
        self.dash_console.print_(0,1, defense_string)
        self.dash_console.print_(0,2, damage_string)
        self.dash_console.print_(0,3, xp_string)

    def update_dash_console(self):
        self.render_stats_to_console()
        pass
