# Provides Regular Chest Model for acquiring items through a container of sorts
# chest.py
# Author: Michael Navazhylau

import tcod
from engine.gameobjects import Entity
from engine.items import Item

class Chest(Entity):

    def __init__(self, x, y, name = "chest", open_chr = "&", close_chr = "#", color = (153, 51, 0), game, chest_item = None, opened = False):
        self.open_chr = open_chr
        self.close_chr = close_chr
        self.opened = opened
        self.chest_item = chest_item

        # Set the character chest character
        entity_chr = open_chr
        if (self.opened):
            entity_chr = open_chr
        else:
            entity_chr = close_chr

        # Base Entity props
        Entity.__init__(self, x, y, name, chr = close_chr, color, combat_behavior = None, game = game, entity_type = "chest")


    def open_chest(self, recipient):

        # TODO if item is None, the chest was is empty

        # DEBUG show message of recipient recieving item

        # TODO interact with inventory system

        #
        self.opened = True
        self.chr = self.open_chr

    def close_chest(self):
        self.opened = False
        self.chr = self.close_chr
