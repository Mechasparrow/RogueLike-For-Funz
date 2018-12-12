import tcod

from .tile import Tile

class GameMap:

    def __init__(self, width, height, fov = True):

        self.width = width
        self.height = height
        self.tiles = GameMap.generate_empty_tiles(self.width, self.height)

        if (fov == True):
            self.fov_map = GameMap.generate_starting_fov_map(self.width, self.height)
            self.update_fov_map()
        else:
            self.fov_map = None


    # Generates a 2d list of basic tiles
    def generate_empty_tiles(width, height):

        tiles_list = []

        for x in range (0, width):
            tile_column = []
            for y in range(0, height):
                tile_column.append(Tile())

            tiles_list.append(tile_column)

        return tiles_list


    # Generate an initial fov map
    def generate_starting_fov_map(width, height):
        return tcod.map.Map(width, height)

    # Updates the fov map
    def update_fov_map(self):
        if (self.fov_map):
            for x in range(0, self.width):
                for y in range(0, self.height):
                    self.fov_map.transparent[y, x] = not (self.tiles[x][y].block_visibility)
                    self.fov_map.walkable[y, x] = self.tiles[x][y].walkable

    # Compute Fov Map
    def compute_fov_map(self, x, y, radius, light_walls = True, algorithm = 0):
        if (self.fov_map):
            self.fov_map.compute_fov(x, y, radius, light_walls, algorithm)

    # Gets a tile from the map
    def getTile(self,x, y):

        return self.tiles[x][y]

    # Updates a tile on the map
    def updateTile(self, x, y, tile):
        self.tiles[x][y] = tile
