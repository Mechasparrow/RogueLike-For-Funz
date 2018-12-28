# Purpose: Util functions for rendering a menu
# menu_renderer.py
# Author: Michael Navazhylau

# import libs
import tcod

def render_menu_system(con, menu_system):
    '''
    renders a menu system to the console
    '''

    if (menu_system.selected_menu_screen != None):
        render_menu_screen(con, menu_system.selected_menu_screen)


def render_menu_screen(con, menu_screen):
    '''
    renders a menu screen to the console
    '''

    menu_title = menu_screen.screen_name
    upper_padding = 6


    con.print_(x=menu_screen.screen_width // 2 - (len(menu_title) // 2), y=upper_padding, string = menu_title)

    item_offset = 0
    for menu_item in menu_screen.menu_options:
        render_menu_item(con, menu_screen.screen_width, menu_screen.screen_height, menu_item, y_offset = item_offset, selected = (menu_item is menu_screen.selected_menu_option))
        item_offset += 2

def render_menu_item(con, screen_width, screen_height, menu_item, y_offset = 0, selected_marker = None, selected = False):
    '''
    renders a menu item to the console
    '''
    marker = ""

    if (selected_marker == None):
        marker = ">"

    if (selected == True):
        item_text = marker + menu_item.text
    else:
        item_text = menu_item.text

    con.print_(x = screen_width // 4, y = screen_height // 4 + y_offset, string = item_text)
