# Purpose: Util functions for rendering gameobjects
# gameobject_renderer.py
# Author: Michael Navazhylau

# import libs
import tcod

# Render the list of gameobjects to a console with a potential fov map taken into account
def render_gameobjects(con, objects, fov_map = None):
    for object in objects:
        render_object = True

        if (fov_map):
            in_fov = fov_map.fov[object.y][object.x]
            render_object = in_fov
        if (render_object):
            render_gameobject(con, object)

# Clear a list of gameobjects from a console
def clear_gameobjects(con, objects):
    for object in objects:
        clear_gameobject(con, object)

# Render a gameobject to a console
def render_gameobject(con, object):
    # Set the color
    tcod.console_set_default_foreground(con, object.color)
    # Draw the object rep on to the console
    tcod.console_put_char(con, object.x, object.y, object.chr, tcod.BKGND_NONE)

# Clear a gameobject from a console
def clear_gameobject(con, object):
    # Set the color
    tcod.console_set_default_foreground(con, object.color)
    # Draw the object rep on to the console
    tcod.console_put_char(con, object.x, object.y, " ", tcod.BKGND_NONE)
