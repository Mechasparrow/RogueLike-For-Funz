import tcod

class Tile:

    def __init__(self, x, y, walkable = False, blocking = False, block_visibility = False, explored = False):

        self.x = x
        self.y = y
        self.walkable = walkable
        self.blocking = blocking
        self.block_visibility = block_visibility
        self.explored = explored
