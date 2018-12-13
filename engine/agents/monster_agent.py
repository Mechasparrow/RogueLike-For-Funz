import tcod

from .intelligent_agent import IntelligentAgent

class MonsterAgent(IntelligentAgent):

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None, ai_target = None):
        IntelligentAgent.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = None)
        self.ai_target = ai_target

    def from_gameobject(gameobject, combat_behavior = None):
        gameobject_monster_agent = MonsterAgent(gameobject.x, gameobject.y, gameobject.name, gameobject.chr, gameobject.color, combat_behavior = combat_behavior, game = gameobject.game)
        print (combat_behavior)
        return gameobject_monster_agent

    # pathfinding for monster + attacking TODO
    def ai_behavior(self):
        target = self.ai_target
        combat_behavior = self.combat_behavior

        fov_map = self.game.map.fov_map

        # Only trigger ai if in FOV
        if (fov_map.fov[self.y][self.x] == False):
            return

        # Dont do anything if no target
        if (target == None or self.combat_behavior.dead):
            return

        path = tcod.path_new_using_map(fov_map, dcost = 0)
        tcod.path_compute(path, self.x, self.y, target.x, target.y)

        (next_x, next_y) = tcod.path_walk(path, recompute = True)

        if (next_x and next_y):
            dx = next_x - self.x
            dy = next_y - self.y

            predicted_pos_x = self.x + dx
            predicted_pos_y = self.y + dy

            gameobjects_at_next_position = self.game.find_gameobjects_at_point(predicted_pos_x, predicted_pos_y)

            if (len(gameobjects_at_next_position) > 0):

                for gameobject in gameobjects_at_next_position:
                    if (gameobject == target):
                        # Dont move there instead attack
                        if (target.combat_behavior):
                            target_behavior = target.combat_behavior
                            print ("preparing to attack")
                            self.combat_behavior.attack(target_behavior)
            else:
                self.move(dx, dy)
