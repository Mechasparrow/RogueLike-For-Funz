class Rect:
    # initliaze the rectangle
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return ("Rect: " + str(self.x) + "," + str(self.y) + "," + str(self.w) + "," + str(self.h))


    # Gives us the center point
    def center(self):
        center_x = self.x + (self.w) // 2
        center_y = self.y + (self.h) // 2

        return (center_x, center_y)
