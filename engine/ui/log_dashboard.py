# Purpose: Dashboard Model for Displaying Log of game messages
# log_dashboard.py
# Author: Michael Navazhylau

# import lib
import tcod

# Extends from DashboardBase
from .dashboard import DashboardBase

class LogDashboard(DashboardBase):

    # Same params as DashboardBase
    # with additional parameter of messages display a message log

    def __init__(self, x, y, width, height, messages = [], dashboard_name = None, visible = True):
        DashboardBase.__init__(self, x, y, width, height, visible, dashboard_name = dashboard_name, dashboard_type = "log")
        self.messages = messages

    # Logs the messages to the message log
    def log_message(self, message):
        self.messages.append(message)

    # renders the border box to the dashboard console
    def render_border_box(self):

        tcod.console_set_default_background(self.dash_console, tcod.black)

        for dx in range(0, self.width):
            tcod.console_set_char_background(self.dash_console, dx, 0, (255,255,255), tcod.BKGND_SET)
            tcod.console_set_char_background(self.dash_console, dx, self.height - 1, (255,255,255), tcod.BKGND_SET)


        for dy in range(0, self.height):
            tcod.console_set_char_background(self.dash_console, 0, dy, (255,255,255), tcod.BKGND_SET)
            tcod.console_set_char_background(self.dash_console, self.width - 1, dy, (255,255,255), tcod.BKGND_SET)




    # render last x amount of messages to dash console
    def render_log_messages(self):

        w_margin = 2
        h_margin = 3

        max_messages = self.height - (2 * h_margin)
        message_count = len(self.messages)

        if (message_count > max_messages):
            message_count = max_messages

        for i in range (0, message_count):
            message = list(reversed(self.messages))[i]
            self.dash_console.print_(w_margin, self.height - i - h_margin, message)

    # updates the console dash
    def update_dash_console(self):
        # TODO render a border box
        self.render_border_box()

        # TODO Render the last 10 messages
        self.render_log_messages()
