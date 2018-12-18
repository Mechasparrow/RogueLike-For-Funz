# Purpose: Model for representing a font
# font.py
# Author: Michael Navazhylau

# Import libs
import tcod

class Font:

    #params
    # path to font file
    # font options
    def __init__(self, path, options):
        self.path = path
        self.options = options
