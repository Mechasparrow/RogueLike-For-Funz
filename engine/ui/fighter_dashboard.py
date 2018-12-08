import tcod

from .dashboard import DashboardBase

class FighterDashboard(DashboardBase):

    def __init__(self, x, y, width, height, fighter, visible = True):
        DashboardBase.__init__(self, x, y, width, height, visible)
        self.fighter = fighter

    def render_fighter_to_console(self):
        health = self.fighter.health
        defense = self.fighter.defense
        damage = self.fighter.damage

        health_string = "Health: " + str(health)
        defense_string = "Defense: " + str(defense)
        damage_string = "Damage: " + str(damage)

        self.dash_console.print_(0,0, health_string)
        self.dash_console.print_(0,1, defense_string)
        self.dash_console.print_(0,2, damage_string)


    def draw(self, console_out):
        self.render_fighter_to_console()
        DashboardBase.draw(self, console_out)
