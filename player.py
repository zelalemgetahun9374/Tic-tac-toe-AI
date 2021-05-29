from abc import ABC, abstractmethod
from time import sleep
import random
import math


class Player(ABC):
    def __init__(self, letter):
        self.letter = letter

    @abstractmethod
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        while True:
            square = input(f"{self.letter}'s turn. Enter your move (0 - 8): ")

            try:
                square = int(square)

                if square not in game.available_moves():
                    raise ValueError

                return square
            except:
                print("Invalid move. Try again!")


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        print(f"{self.letter}'s turn. Move: {square}")
        sleep(0.5)  # wait for 0.5 seconds
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            print('available moves')
            print(game.available_moves())
            square = random.choice(game.available_moves())
        else:
            square = self.minmax(game, self.letter)['position']

        print(f"{self.letter}'s turn. Move: {square}")
        sleep(0.5)  # wait for 0.5 seconds
        return square

    # use the maximize minimize algorithm
    def minmax(self, game, player):
        max_player = self.letter
        other_player = 'X' if player == 'O' else 'O'

        if game.winner == other_player:
            return {'position': None, 'score': 1 * (game.num_empty_squares() + 1) if other_player == self.letter else -1 * (game.num_empty_squares() + 1)}

        if not game.num_empty_squares():
            return {'position': None, 'score': 0}

        if player == self.letter:
            best = {'position': None, 'score': -math.inf}  # maximize our score
        else:
            # minimize opponent's score
            best = {'position': None, 'score': math.inf}

        for possible_move in game.available_moves():
            game.make_move(possible_move, player)
            simulation = self.minmax(game, other_player)

            # indicates the next optimal move
            simulation['position'] = possible_move
            game.board[possible_move] = ' '  # remove simulated move
            game.winner = None  # set winner back to None

            if player == self.letter:
                if simulation['score'] > best['score']:
                    best = simulation
            else:
                if simulation['score'] < best['score']:
                    best = simulation

        return best
