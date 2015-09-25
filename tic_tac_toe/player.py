#Este archivo fue ediado para comprobar las características colaboratibas de GitHub - Álvaro Sánchez Díaz

"""
The canonical player of our game. Just subclass and implement make_move
in order to modify behavior or write AI players. This class depends on
the io module in order to get the player's move from the command-line.
"""

import io

class Player:
  def __init__(self, symbol):
    self.symbol = symbol

  def make_move(self, game):
    game.make_move(io.get_move(), self.symbol)
