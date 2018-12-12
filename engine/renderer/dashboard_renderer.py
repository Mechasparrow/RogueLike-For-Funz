import tcod

def render_dashboards(con, dashboards):
    for dashboard in dashboards:
        if (dashboard.visible):
            draw_dashboard(con, dashboard)

def clear_dashboards(con, dashboards):
    for dashboard in dashboards:
        clear_dashboard(con, dashboard)

def draw_dashboard(con, dashboard):
    dashboard.update_dash_console()
    tcod.console_blit(dashboard.dash_console, 0, 0, dashboard.width, dashboard.height, con, dashboard.x, dashboard.y)

def clear_dashboard(con, dashboard):
    dashboard.dash_console.clear()
    tcod.console_blit(dashboard.dash_console, 0, 0, dashboard.width, dashboard.height, con, dashboard.x, dashboard.y)
