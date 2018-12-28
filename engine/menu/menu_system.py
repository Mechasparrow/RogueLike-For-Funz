# Purpose: Represents a system of menus
# menu_system.py
# Author: Michael Navazhylau

from .menu_screen import MenuScreen

class MenuSystem:

    def __init__(self, menu_width, menu_height, menu_screens=None, default_menu_screen_idx=None, game = None):
        '''
        Takes in a list menu screens
        Requires a index of starting menu screen
        Has its own associated renderer system in renderer sublib
        '''

        # game ref
        self.game = game

        # width + height
        self.menu_width = menu_width
        self.menu_height = menu_height

        # If the no screens specified set to empty list
        if (menu_screens == None):
            self.menu_screens = [MenuScreen(screen_width = self.menu_width, screen_height = self.menu_height, screen_name="Main Menu")]
            self.selected_menu_screen = self.menu_screens[0]
        else:
            self.menu_screens = menu_screens
            if (default_menu_screen_idx == None and len(self.menu_screens) > 0):
                self.selected_menu_screen = self.menu_screens[0]
            else:
                self.selected_menu_screen = self.menu_screens[default_menu_screen]

    def handle_menu_interaction(self, game, action):
        '''
        Handle the menu interactions
        '''

        if (action == "menu_up"):
            selected_menu_item_idx = self.selected_menu_screen.get_selected_option_idx()
            new_menu_idx = selected_menu_item_idx

            if (selected_menu_item_idx > 0):
                new_menu_idx -= 1

            self.selected_menu_screen.set_selected_option_by_idx(new_menu_idx)
        elif (action == "menu_down"):
            selected_menu_item_idx = self.selected_menu_screen.get_selected_option_idx()
            new_menu_idx = selected_menu_item_idx

            if (selected_menu_item_idx < (len(self.selected_menu_screen.menu_options) - 1)):
                new_menu_idx += 1

            self.selected_menu_screen.set_selected_option_by_idx(new_menu_idx)
        elif (action == "menu_select"):
            selected_menu_option = self.selected_menu_screen.selected_menu_option
            selected_menu_option.perform_menu_action(self.game)
