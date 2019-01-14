# Purpose: Base Model for Dashboards
# dashboard.py
# Author: Michael Navazhylau

# import libs
import tcod

class DashboardBase:

    # params
    # position + width and height of dashboard
    # whether dashboard is visible (boolean)
    def __init__(self, x, y, width, height, visible = True, dashboard_name = None, dashboard_type = "base"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        self.dashboard_name = dashboard_name
        self.dashboard_type = dashboard_type

        # create a console to handle this dashboard
        self.dash_console = tcod.console.Console(self.width, self.height)

    # hide the dashboard
    def hide_dashboard(self):
        self.visible = False

    # show the dashboard
    def show_dashboard(self):
        self.visible = True

    # Abstract method
    # Update the dashboard console text, images, etc
    def update_dash_console(self):

        pass
