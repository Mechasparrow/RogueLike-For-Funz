import tcod

#General game props
GAME_FPS = 15

# console props
SCREEN_WIDTH=160
SCREEN_HEIGHT=80
TITLE = "RogueBird"

# Font
FONT='font_images/arial12x12.png'
FONT_FLAGS = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD

# Tile colors
color_walkable_tile = (102, 102, 255)
color_walkable_dark_tile = (50,50,100)
color_dark_wall = (153, 51, 102)
color_light_wall = (255, 80, 80)

# Monster colors
monster_basic_color = (9, 232, 53)
monster_itermediate_color = (224, 232, 9)
monster_advanced = (232, 31, 9)
