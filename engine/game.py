import tcod

from .mapping.tile import *
from .renderer.renderer import Renderer

class Game:

    def __init__(self, game_name, window_width, window_height, font, fps = None):
        # Game console props
        self.game_name = game_name
        self.window_width = window_width
        self.window_height = window_height
        self.font = font
        self.fps = fps

        if (self.fps != None):
            tcod.sys_set_fps(self.fps)

        # Initialize font
        tcod.console_set_custom_font(
            self.font.path,
            self.font.options
        )

        # Initialize root console
        self.root_console = tcod.console_init_root(self.window_width, self.window_height, self.game_name)

        # Initially game is not running
        self.running = False

        # Additional props
        self.props = {}

        # Game objects
        self.objects = []

        # Dashboards
        self.dashboards = []

        # World map
        self.map = Game.gen_walkable_map(80,60)
        self.fov_map = tcod.map.Map(80, 60)

        # Input handlers
        self.input_handlers = []

        #Renderer
        self.game_renderer = Renderer(self)

    def update_fov_map(self):


        for x in range(0, 80):
            for y in range(0, 60):
                self.fov_map.transparent[y, x] = not (self.map[x][y].block_visibility)
                self.fov_map.walkable[y,x] = self.map[x][y].walkable

        self.fov_map.transparent[30,30] = False


    def gen_walkable_map(width, height):
        walkable_map = []

        for x in range(0,width):
            walkable_column = []
            for y in range (0,height):
                walkable_column.append(Tile(x, y))

            walkable_map.append(walkable_column)

        return walkable_map

    def add_input_handler(self, input_handler):
        self.input_handlers.append(input_handler)

    def handle_inputs(self):

        key = tcod.console_check_for_keypress()

        for handler in self.input_handlers:
            handler.handle_input(key.vk)

    # TODO see if further abstraction needed
    # Adds a gameobject to the game
    def add_gameobject_to_game(self,gb):
        self.objects.append(gb)

    # returns a list of game objects by their name
    def find_gameobjects_by_name(self, name):

        # filter function by gameobject name
        def filter_by_name(object):
            if (object.name == name):
                return True
            else:
                return False

        #return the filtered game objects
        filtered_gameobjects = list(filter(filter_by_name, self.objects))

        return filtered_gameobjects

    # return a list of game objects at a specific point
    def find_gameobjects_at_point(self,x, y):

        # filter function by object position
        def filter_by_point(object):
            if (object.x == x and object.y == y):
                return True
            else:
                return False

        filtered_gameobjects = list(filter(filter_by_point, self.objects))
        return filtered_gameobjects

    # Adds a dashboard to the game
    def add_dashboard_to_game(self, dashboard):
        self.dashboards.append(dashboard)

    # Start the main game loop
    def start_loop(self, logic):
        self.running = True


        while(self.running):
            logic(self)

            # Render system
            self.game_renderer.render_all()
            self.game_renderer.update_console()
            self.game_renderer.clear_all()


    # Stop the loop
    def stop_loop(self):
        self.running = False
