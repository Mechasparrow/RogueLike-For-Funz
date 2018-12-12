import tcod

def render_gameobjects(con, objects, fov_map = None):
    for object in objects:
        render_object = True
        if (fov_map):
            in_fov = fov_map.fov[object.y][object.x]
            render_object = in_fov
        if (render_object):
            render_gameobject(con, object)

def clear_gameobjects(con, objects):
    for object in objects:
        clear_gameobject(con, object)


def render_gameobject(con, object):
    # Set the color
    tcod.console_set_default_foreground(con, object.color)
    # Draw the object rep on to the console
    tcod.console_put_char(con, object.x, object.y, object.chr, tcod.BKGND_NONE)

def clear_gameobject(con, object):
    # Set the color
    tcod.console_set_default_foreground(con, object.color)
    # Draw the object rep on to the console
    tcod.console_put_char(con, object.x, object.y, " ", tcod.BKGND_NONE)
