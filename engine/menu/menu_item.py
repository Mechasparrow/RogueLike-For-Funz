# Purpose: Represents a item on a menu
# menu_system.py
# Author: Michael Navazhylau

class MenuItem:

    def __init__(self, text, menu_action=None):
        """
        Represents an selectable item on a menu
        """

        self.text = text

        if (menu_action == None):
            self.menu_action = self.dummy_menu_action
        else:
            self.menu_action = menu_action

    def dummy_menu_action(self, game):
        '''
        Does nothing
        '''
        pass

    def perform_menu_action(self, game):
        """
        Performs the action of the menu item
        """
        print ("performing menu action")
        self.menu_action(game)
