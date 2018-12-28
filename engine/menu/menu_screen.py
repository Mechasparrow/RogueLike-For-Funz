# Purpose: Represents a screen of a menu
# menu_screen.py
# Author: Michael Navazhylau

class MenuScreen:

    def __init__(self, screen_width, screen_height, screen_name=None, menu_options=None, selected_menu_option_idx=None):
        """
        Represents a screen on a menu
        Has a list of menu options
        Extra spice if one chooses... IDK yet
        """

        # Menu Screen name
        self.screen_name = screen_name
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Handles menu options
        if (menu_options == None):
            self.menu_options = []
            self.selected_menu_option = None
        else:
            self.menu_options = menu_options
            if (selected_menu_option_idx == None):
                self.selected_menu_option = None
            else:
                self.selected_menu_option = self.menu_options[self.selected_menu_option_idx]

    def get_selected_option_idx(self):
        '''
        returns the selected menu option
        '''
        return self.menu_options.index(self.selected_menu_option)

    def set_selected_option(self, selected_option):
        '''
        Set the selected menu option
        Takes in the option to select
        '''
        self.selected_menu_option = selected_option

    def set_selected_option_by_idx(self, idx):
        '''
        Sets the selected menu option by the index of the option in the option list
        '''

        menu_option = self.menu_options[idx]
        self.set_selected_option(menu_option)
