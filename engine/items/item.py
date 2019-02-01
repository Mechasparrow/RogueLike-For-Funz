# Provides Base Item Model for inventory system and chests and whatever other potential usage
# item.py
# Author: Michael Navazhylau

class Item:

    # constructor for item model
    #params
    # name of item
    # item type
    # stackable: Can the item be stacked on top of itself (i.e Potions, Arrows, etc)
    def __init__(self, name, description = None, item_type = "basic", stack_limit = 1):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.stack_limit = stack_limit


    #serialization + parsing
    def as_dictionary(self):
        return {
            'name': self.name,
            'description': self.description,
            'item_type': self.item_type,
            'stack_limit': self.stack_limit
        }

    def from_dictionary(item_dict, g):
        if (item_dict == None):
            return None

        print (item_dict)
        item = Item(name = item_dict['name'], description = item_dict['description'], item_type = item_dict['item_type'], stack_limit = item_dict['stack_limit'])

    # Uses the item
    def use_item(self, recipient):

        pass
