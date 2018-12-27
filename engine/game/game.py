# Purpose: Main Game Model that keeps track of everything
# game.py
# Author: Michael Navazhylau

# import libs
import tcod

# polyfill
import sys
sys.path.append("..")

# Utils
from .dashboard_utils import *

# Floor gen
from engine.floors import Floor
from engine.floors import FloorManager

# Map
from engine.mapping.game_map import GameMap

# Renderer
from engine.renderer import Renderer

# UI
from engine.ui import LogDashboard


class Game:

    # params
    # name of game, width of console window, height of console window, game font, game fps

    def __init__(self, game_name, window_width, window_height, font, fps = None, floor_manager = None, message_log = True):
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

        # Floor handling DEBUG bring into own handler class
        if (floor_manager is None):
            self.floor_manager = FloorManager((self.window_width * 3) // 4, self.window_height, game = self)


        # Dashboards
        self.dashboards = []

        if (message_log == True):
            margin = 4
            message_log_dashboard = LogDashboard((self.window_width * 3) // 4,margin, self.window_width // 4, self.window_height - margin, messages = [])
            add_dashboard_to_game(self, message_log_dashboard)
        # World map
        # TODO make the map width + height configurable
        #self.map = GameMap((self.window_width * 3) // 4, self.window_height) DEAD

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
