# Purpose: Util functions for rendering dashboards
# dashboard_renderer.py
# Author: Michael Navazhylau

# import libs
import tcod

# render dashboards to a console
def render_dashboards(con, dashboards):
    for dashboard in dashboards:
        if (dashboard.visible):
            draw_dashboard(con, dashboard)

# Clear dashboards from a console
def clear_dashboards(con, dashboards):
    for dashboard in dashboards:
        clear_dashboard(con, dashboard)
        
# Draw a dashboard to the console
def draw_dashboard(con, dashboard):
    dashboard.update_dash_console()
    tcod.console_blit(dashboard.dash_console, 0, 0, dashboard.width, dashboard.height, con, dashboard.x, dashboard.y)

# Clear a dashboard from a console
def clear_dashboard(con, dashboard):
    dashboard.dash_console.clear()
    tcod.console_blit(dashboard.dash_console, 0, 0, dashboard.width, dashboard.height, con, dashboard.x, dashboard.y)
