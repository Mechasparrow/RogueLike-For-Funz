import tcod

from .dashboard import DashboardBase

class CustomMessageDashboard(DashboardBase):

    def __init__(self, x, y, width, height, message = "", visible = True):
        DashboardBase.__init__(self, x, y, width, height, visible)
        self.message = message

    def set_message(self, message):
        self.message = message

    def render_message(self):
        self.dash_console.print_(0,0, self.message)

    def draw(self, console_out):
        self.render_message()
        DashboardBase.draw(self, console_out)
