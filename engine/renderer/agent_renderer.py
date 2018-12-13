from .gameobject_renderer import *

def render_agents(con, agents, fov_map = None):
    for object in objects:
        render_object = True
        if (fov_map):
            in_fov = fov_map.fov[object.y][object.x]
            render_object = in_fov
        if (render_object):
            render_gameobject(con, object)

def clear_agents(con, agents):
    clear_gameobjects(con, agents)

def render_agent(con, agent):
    if (agent.dead):
        # Set the color
        tcod.console_set_default_foreground(con, (0,255,0))
        # Draw the object rep on to the console
        tcod.console_put_char(con, object.x, object.y, %, tcod.BKGND_NONE)
    else:
        render_gameobject(con, agent)

def render_agent(con, object, map):
    # Set the color
    tcod.console_set_default_foreground(con, object.color)
    # Draw the object rep on to the console
    tcod.console_put_char(con, object.x, object.y, object.chr, tcod.BKGND_NONE)



def clear_agent(con, object):
    clear_gameobject(con, object)
