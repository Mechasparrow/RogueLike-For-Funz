# Purpose: Main Game Model that keeps track of everything
# game.py
# Author: Michael Navazhylau

# import libs
import tcod

# polyfill
import sys
sys.path.append("..")

# Map
from engine.mapping.game_map import GameMap

# Renderer
from engine.renderer import Renderer

class Game:

    # params
    # name of game, width of console window, height of console window, game font, game fps

    def __init__(self, game_name, window_width, window_height, font, fps = None):
        # Game console props
        self.game_name = game_name
        self.window_width = window_width
        self.window_height = window_height
        self.font = font
        self.fps = fps

        # if the game had fps specified, update the console fps
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
        # TODO make the map width + height configurable
        self.map = GameMap(60, 80)

        # Input handlers
        self.input_handlers = []

        #Renderer
        self.game_renderer = Renderer(game = self)

    # Start the main game loop
    def start_loop(self, logic):
        # set the game to be running
        self.running = True

        # game loop
        while(self.running):
            # game logic
            logic(self)

            # TODO
            # run through all the input handlers

            # Render
            self.game_renderer.render_all()
            self.game_renderer.update_console()
            self.game_renderer.clear_all()


    # Stop the game loop
    def stop_loop(self):
        self.running = False
