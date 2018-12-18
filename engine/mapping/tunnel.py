# Purpose: Allow tunnels to be drawn between to points in space
# tunnel.py
# Author: Michael Navazhylau

# TODO make tunnel code look cleaner

# Tile util
from .tile import Tile

class Tunnel:

    # @params
    # first point
    # second point
    # tunnel orientation "h"orizontal or "v"ertical
    def __init__(self, point1, point2, orientation = "h"):
        self.point1 = point1
        self.point2 = point2
        self.orientation = orientation

    # draw a tunnel and place it onto a map
    def draw_tunnel(self, map):
        if (self.orientation == "h"):
            self.draw_h_tunnel(map)

        elif (self.orientation == "v"):
            self.draw_v_tunnel(map)

    # Draw a vertical tunnel between two points
    def draw_v_tunnel(self,map):
        dx = (self.point2[0] - self.point1[0])
        print (dx)

        dy = abs(self.point2[1] - self.point1[1])

        x = self.point1[0]

        mid_way = self.point1[1] + (dy // 2)

        # tunnel loop
        for y in range(self.point1[1], self.point2[1]):

            if (y != self.point1[1] and y != (self.point2[1] - 1)):
                map[x+1][y] = Tile(blocking = True, block_visibility = True)
                map[x-1][y] = Tile(blocking = True, block_visibility = True)

            map[x][y] = Tile(walkable = True)

            # midway tunnel
            if (y == mid_way):

                # Edge cases

                if (dx > 0):
                    map[x-1][y+1] = Tile( blocking =True, block_visibility = True)
                    map[x][y+1] = Tile( blocking =True, block_visibility = True)
                    map[x+dx+1][y-1] = Tile( blocking =True, block_visibility = True)
                    map[x+dx+1][y] = Tile(blocking =True, block_visibility = True)
                elif (dx < 0):
                    map[x][y+1] = Tile(blocking = True, block_visibility = True)
                    map[x+1][y+1] = Tile(blocking = True, block_visibility = True)
                    map[x+dx-1][y] = Tile(blocking = True, block_visibility = True)
                    map[x+dx-1][y-1] = Tile( blocking = True, block_visibility = True)


                for i in range(0, abs(dx)):



                    if (dx > 0):
                        x += 1

                        if (x > self.point1[0] and x <= self.point2[0]):
                            map[x][y+1] = Tile( blocking = True, block_visibility = True)
                            map[x][y-1] = Tile( blocking = True, block_visibility = True)

                    if (dx < 0):
                        x -= 1

                        if (x < self.point1[0] and x >= self.point2[0]):
                            map[x][y+1] = Tile( blocking = True, block_visibility = True)
                            map[x][y-1] = Tile( blocking = True, block_visibility = True)


                    map[x][y] = Tile(walkable = True)

    # draw a horizontal tunnel between two points
    def draw_h_tunnel(self,map):
        dx = abs(self.point2[0] - self.point1[0])
        dy = (self.point2[1] - self.point1[1])


        mid_way = self.point1[0] + (dx // 2)

        y = self.point1[1]


        # loop to draw tiles onto map
        for x in range(self.point1[0], self.point2[0]):
            # Draw walls for tunnel
            if (x != self.point1[0] and x != (self.point2[0] - 1)):
                map[x][y-1] = Tile( blocking = True, block_visibility = True)
                map[x][y+1] = Tile( blocking = True, block_visibility = True)

            map[x][y] = Tile( walkable = True)


            # midway tunnel
            if (x == mid_way):

                if (dy > 0):
                    # Fix special edges
                    map[x+1][y] = Tile( blocking = True, block_visibility = True)
                    map[x+1][y-1] = Tile( blocking = True, block_visibility = True)
                    map[x][y+dy+1] = Tile(blocking = True, block_visibility = True)
                    map[x-1][y+dy+1] = Tile( blocking = True, block_visibility = True)
                elif (dy < 0):
                    map[x+1][y] = Tile( blocking = True, block_visibility = True)
                    map[x+1][y+1] = Tile( blocking = True, block_visibility = True)
                    map[x][y+dy-1] = Tile(blocking = True, block_visibility = True)
                    map[x-1][y+dy-1] = Tile(blocking = True, block_visibility = True)

                for i in range(0, abs(dy)):
                    if (dy > 0):
                        y += 1

                        if (y >= self.point1[1] and y <= (self.point1[1] + dy)):
                            map[x+1][y] = Tile(blocking = True, block_visibility = True)
                            map[x-1][y] = Tile( blocking = True, block_visibility = True)

                    if (dy < 0):
                        y -= 1

                        if (y <= self.point1[1] and y >= (self.point1[1] + dy)):
                            map[x+1][y] = Tile(blocking = True, block_visibility = True)
                            map[x-1][y] = Tile( blocking = True, block_visibility = True)

                    map[x][y] = Tile(walkable = True)
