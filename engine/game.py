import tcod

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

        # Input handlers
        self.input_handlers = []


    def add_input_handler(self, input_handler):
        self.input_handlers.append(input_handler)

    def handle_inputs(self):

        key = tcod.console_check_for_keypress()

        for handler in self.input_handlers:
            handler.handle_input(key)

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

    # Render the game objects and other components to screen
    def render(self):
        for object in self.objects:
            object.draw(self.root_console)

    def clear_render(self):
        for object in self.objects:
            object.clear(self.root_console)


    # Start the main game loop
    def start_loop(self, logic):
        self.running = True


        while(self.running):
            logic(self)

            self.handle_inputs()

            self.render()
            tcod.console_flush() # Show the console
            self.clear_render()

    # Stop the loop
    def stop_loop(self):
        self.running = False
