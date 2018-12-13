from .agent_utils import *

class GameTurnHandler:
    def __init__(self, game):
        self.game = game

    def take_turn(self):
        agents = get_game_agents(self.game)
        for agent in agents:
            agent.ai_behavior()
