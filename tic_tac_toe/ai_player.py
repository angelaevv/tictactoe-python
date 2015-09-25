#Este archivo fue ediado para comprobar las características colaboratibas de GitHub - Álvaro Sánchez Díaz

"""
An AI player of our game. Subclasses Player and implements the simplest
(i.e. dumbest) AI algorithm: make a move at random.
"""

import random
from player import Player

class AIPlayer(Player):
  def make_move(self, game):
    game.make_move(random.choice(game.valid_moves()), self.symbol)
