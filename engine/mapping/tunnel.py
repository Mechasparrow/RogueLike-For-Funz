from .tile import Tile

class Tunnel:

    def __init__(self, point1, point2, orientation = "h"):

        self.point1 = point1
        self.point2 = point2
        self.orientation = orientation


    def draw_tunnel(self, map):

        if (self.orientation == "h"):

            dx = abs(self.point2[0] - self.point1[0])
            dy = (self.point2[1] - self.point1[1])


            mid_way = self.point1[0] + (dx // 2)

            y = self.point1[1]


            for x in range(self.point1[0], self.point2[0]):
                # Draw walls for tunnel
                if (x != self.point1[0] and x != (self.point2[0] - 1)):
                    map[x][y-1] = Tile(x, y-1, blocking = True)
                    map[x][y+1] = Tile(x, y+1, blocking = True)

                map[x][y] = Tile(x, y, walkable = True)


                if (x == mid_way):

                    if (dy >= 0):
                        # Fix special edges
                        map[x+1][y] = Tile(x+1, y, blocking = True)
                        map[x+1][y-1] = Tile(x+1, y-1, blocking = True)
                        map[x][y+dy+1] = Tile(x, y+dy+1, blocking = True)
                        map[x-1][y+dy+1] = Tile(x-1, y+dy+1, blocking = True)


                    for i in range(0, dy):
                        if (dy > 0):
                            y += 1
                        if (dy < 0):
                            y -= 1
                            print ("less")

                        if (y >= self.point1[1] and y <= (self.point1[1] + dy)):
                            map[x+1][y] = Tile(x+1, y, blocking = True)
                            map[x-1][y] = Tile(x-1, y, blocking = True)

                        # if (y == (self.point[1] + dy)):

                        map[x][y] = Tile(x, y, walkable = True)

        elif (self.orientation == "v"):
            dx = (self.point2[0] - self.point1[0])
            print (dx)

            dy = abs(self.point2[1] - self.point1[1])

            x = self.point1[0]

            mid_way = self.point1[1] + (dy // 2)

            for y in range(self.point1[1], self.point2[1]):

                if (y != self.point1[1] and y != (self.point2[1] - 1)):
                    map[x+1][y] = Tile(x+1, y, blocking = True)
                    map[x-1][y] = Tile(x-1, y, blocking = True)

                map[x][y] = Tile(x, y, walkable = True)

                if (y == mid_way):
                    for i in range(0, dx):

                        if (dx > 0):
                            x += 1
                        if (dx < 0):
                            x -= 1

                        map[x][y] = Tile(x, y, walkable = True)
