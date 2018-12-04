from .rect import Rect
from .tile import Tile

class Room:

    # default initialization of room
    def __init__(self, map, rect):
        self.map = map
        self.rect = rect
        pass

    # Get edges on top and bottom, y position of edge
    def top_edge(self):
        return self.rect.y

    def bottom_edge(self):
        return (self.rect.y + self.rect.h)

    # Get edges on left and right, x position of edge
    def left_edge(self):
        return self.rect.x

    def right_edge(self):
        return (self.rect.x + self.rect.w)


    # create a new room with a position w/ width and height
    def new_room(map, x, y, w, h):
        new_rect = Rect(x,y,w,h)
        return Room(map, new_rect)

    # draw the room
    def draw_room(self):

        # ====
        # |  |
        # ====

        # x-1
        # (x+w)
        # y-1
        # (y+h)

        room_rect = self.rect

        starting_x = room_rect.x - 1
        starting_y = room_rect.y - 1
        ending_x = room_rect.x+room_rect.w
        ending_y = room_rect.y+room_rect.h

        for x in range (starting_x, ending_x + 1):
            for y in range(starting_y, ending_y + 1):

                room_tile = Tile(x,y)

                if (x == starting_x or x == ending_x or y == starting_y or y == ending_y):
                    room_tile.blocking = True
                    room_tile.block_visibility = True

                    try:
                        if ((x == starting_x and self.map[x-1][y].walkable == True) or (y == starting_y and self.map[x][y-1].walkable == True) or (y == ending_y and self.map[x][y+1].walkable == True) or (x == ending_x and self.map[x+1][y].walkable == True)):
                            room_tile.blocking = False
                            room_tile.block_visibility = False
                            room_tile.walkable = True
                    except:
                        pass

                else:

                    room_tile.walkable = True
                    room_tile.blocking = False

                self.map[x][y] = room_tile
