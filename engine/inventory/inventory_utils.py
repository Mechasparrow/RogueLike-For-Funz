# Purpose: Util functions to deal with entity inventories
# inventory_utils.py
# Author: Michael Navazhylau

from engine.items import Item

# DEBUG
def display_inventory_debug(inventory_items):

    print ("An entity has the following items")

    i = 1
    for item in inventory_items:
        print (str(i) + ")" +" " + item.name)
        i+=1
