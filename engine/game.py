class Game:

    def __init__(self, window_width, window_height, font):
        self.running = False
        self.objects = []
        self.props = {}

        self.window_width = window_width
        self.window_height = window_height

        self.root_console = None
        self.font = None


        pass

    def render():

        pass

    def start_loop(self, logic):
        self.running = True

        while(self.running):
            logic(self)

    def stop_loop(self):
        self.running = False
