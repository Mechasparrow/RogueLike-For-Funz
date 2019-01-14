# Purpose: Model for Dashboards with a custom message
# custom_message_dashboard.py
# Author: Michael Navazhylau

# import libs
import tcod

# Extends from DashboardBase
from .dashboard import DashboardBase

class CustomMessageDashboard(DashboardBase):

    # Same params as DashboardBase
    # + additional message parameter for custom message
    def __init__(self, x, y, width, height, message = "", dashboard_name = None, visible = True):
        DashboardBase.__init__(self, x, y, width, height, visible, dashboard_name = dashboard_name, dashboard_type = "custom")
        self.message = message

    # Set the custom message
    def set_message(self, message):
        self.message = message

    # render the custom message to the internal dash console
    def render_message(self):
        self.dash_console.print_(0,0, self.message)

    # update the dash console with the custom message
    def update_dash_console(self):
        self.render_message()
