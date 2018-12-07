import tcod

class Fighter:

    def __init__(self, health, defense, damage, ai = None):
        self.owner = None
        self.health = health
        self.defense = defense
        self.damage = damage
        self.dead = False
        self.path = None


        # AI modifier
        self.ai = ai
        if (self.ai):
            self.ai.owner = self

    def die(self):
        self.dead = True
        self.owner.chr = "%"

    def attack(self,target):
        print (self.owner.name + " has attacked " + target.owner.name)
        target.recieve_hit(self.damage)

    def recieve_hit(self, damage):
        print (self.owner.name + " was hit")

        if ((damage - self.defense) < 0):
            print ("The attack was ineffective!")
        else:
            self.health = self.health - (damage - self.defense)

        print ("Your health is now " + str(self.health))

        if (self.health <= 0):
            self.die()

    # @param Target is a gameobject
    def nav(self, target):
        # dead func
        pass
