import tcod

class Fighter:

    def __init__(self, health, defense, attack):
        self.owner = None
        self.health = health
        self.defense = defense
        self.attack = attack
        self.path = None

    def attack(self,target):
        print (self.owner.name + " has attacked " + target.owner.name)

    def hit(self):
        print (self.owner.name + " was hit")

    def nav(self, target):
        map = self.owner.game.fov_map
        path = tcod.path_new_using_map(map)
        tcod.path_compute(path, self.owner.x, self.owner.y, target.x, target.y)

        (next_x, next_y) = tcod.path_walk(path, recompute = True)

        if (next_x and next_y):
            dx = next_x - self.owner.x
            dy = next_y - self.owner.y

            self.owner.move(dx, dy)
            print (str(dx) + "," + str(dy))


        print (str(self.owner.x) + "," + str(self.owner.y))
        print ("next")
        print (str(next_x) + "," + str(next_y))
