# Purpose: Base Model for Dashboards
# dashboard.py
# Author: Michael Navazhylau

# import libs
import tcod

class DashboardBase:

    # params
    # position + width and height of dashboard
    # whether dashboard is visible (boolean)
    def __init__(self, x, y, width, height, visible = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible

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
