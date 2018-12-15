import tcod

# Map
from engine.mapping.game_map import GameMap

# Renderer
from engine.renderer.renderer import Renderer


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
        self.map = GameMap(60, 80)

        # Input handlers
        self.input_handlers = []

        #Renderer
        self.game_renderer = Renderer(self)

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
