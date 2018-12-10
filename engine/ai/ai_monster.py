import tcod
from .ai_base import BaseAI

# AI for the monster

class MonsterAI(BaseAI):

    def __init__(self, attack_target = None):
        BaseAI.__init__(self)
        self.attack_target = attack_target

    # Monster ai
    def perform_ai(self):
        target = self.attack_target
        fighter = self.owner

        fov_map = fighter.owner.game.fov_map

        # Only trigger ai if in FOV
        if (fov_map.fov[fighter.owner.y][fighter.owner.x] == False):
            return

        # Dont do anything if no target
        if (target == None or fighter.dead):
            return

        map = fighter.owner.game.fov_map
        path = tcod.path_new_using_map(map, dcost = 0)
        tcod.path_compute(path, fighter.owner.x, fighter.owner.y, target.x, target.y)

        (next_x, next_y) = tcod.path_walk(path, recompute = True)

        if (next_x and next_y):
            dx = next_x - fighter.owner.x
            dy = next_y - fighter.owner.y
            print (str(dx) + "," + str(dy))

            predicted_pos_x = fighter.owner.x + dx
            predicted_pos_y = fighter.owner.y + dy

            gameobjects_at_next_position = fighter.owner.game.find_gameobjects_at_point(predicted_pos_x, predicted_pos_y)

            if (len(gameobjects_at_next_position) > 0):

                for gameobject in gameobjects_at_next_position:
                    if (gameobject == target):
                        # Dont move there instead attack
                        if (target.fighter):
                            target_fighter = target.fighter
                            print ("preparing to attack")
                            fighter.attack(target_fighter)
            else:
                fighter.owner.move(dx, dy)

            print (str(dx) + "," + str(dy))


        print (str(fighter.owner.x) + "," + str(fighter.owner.y))
        print ("next")
        print (str(next_x) + "," + str(next_y))
