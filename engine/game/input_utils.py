import tcod

def add_input_handler(game, input_handler):
    game.input_handlers.append(input_handler)

def handle_inputs(game):

    key = tcod.console_check_for_keypress()

    for handler in game.input_handlers:
        handler.handle_input(key.vk)
