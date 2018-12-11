import tcod

class Tile:

    def __init__(self, walkable = False, blocking = False, block_visibility = False, explored = False):
        self.walkable = walkable
        self.blocking = blocking
        self.block_visibility = block_visibility
        self.explored = explored
