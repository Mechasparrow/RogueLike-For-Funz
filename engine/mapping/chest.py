# Provides Regular Chest Model for acquiring items through a container of sorts
# chest.py
# Author: Michael Navazhylau

import tcod
from engine.gameobjects import Entity
from engine.items import Item

class Chest(Entity):

    # Params
    # Same params as entity minus combat_behavior

    # open_chr: the character of the opened chest
    # close_chr: the character of the closed chest
    # chest_item: the item of the chest
    # opened: chest opened


    def __init__(self, x, y, name = "chest", open_chr = "&", close_chr = "#", color = (153, 51, 0), game = None, chest_item = None, opened = False):
        self.open_chr = open_chr
        self.close_chr = close_chr
        self.chest_item = chest_item
        self.opened = opened

        # Set the character chest character
        entity_chr = open_chr
        if (self.opened):
            entity_chr = open_chr
        else:
            entity_chr = close_chr

        # Base Entity props
        Entity.__init__(self, x, y, name = name, chr = close_chr, color = color, combat_behavior = None, game = game, entity_type = "chest")


    def open_chest(self, recipient):
        # Dont do anything if chest is already opened
        if (self.opened == True):
            return

        # TODO if item is None, the chest is empty
        if (self.chest_item == None):
            print ("No item found in chest")
        # DEBUG show message of recipient recieving item
        else:
            if (recipient.type == "Entity"):
                print (str(recipient.name) + " recieved " + str(self.chest_item.name))

                # Empty the chest after being opened by an applicable recipient
                self.chest_item = None

        # TODO interact with inventory system

        #

        self.opened = True
        self.chr = self.open_chr

    def close_chest(self):
        self.opened = False
        self.chr = self.close_chr
