import random
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
from game import TicTacToe


def play(game, x_player, o_player, print_info=True):
    game.print_num_board()
    letter = 'X'
    while game.available_moves():
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        game.make_move(square, letter)

        if print_info:
            game.print_board()
            print("")

        if game.game_won(square, letter):
            if print_info:
                print(f"{letter} won!")
            return letter

        letter = 'O' if letter == 'X' else 'X'

    if print_info:
        print("It is a tie!")


if __name__ == "__main__":
    print('''
      Tic Tac Toe Game
      Choose PLayers
      1. Human vs Random Computer
      2. Human vs Smart Computer
      3. Human vs Human
      4. Random Computer vs Smart Computer
      5. Smart Computer vs Smart Computer
  ''')

    choice = ''
    while choice not in range(1, 6):
        try:
            choice = int(input("Choose players: "))
        except:
            print("Enter valid number")

    if choice == 1:
        print("Human(X) vs Random Computer(O) Game starts ...\n")
        play(TicTacToe(), HumanPlayer('X'), RandomComputerPlayer('O'))
    elif choice == 2:
        print("Human(X) vs Smart Computer(O) Game starts ...\n")
        play(TicTacToe(), HumanPlayer('X'), SmartComputerPlayer('O'))
    elif choice == 3:
        print("Human(X) vs Human(O) Game starts ...\n")
        play(TicTacToe(), HumanPlayer('X'), HumanPlayer('O'))
    elif choice == 4:
        print("Random Computer(X) vs Smart Computer(O) Game starts ...\n")
        play(TicTacToe(), RandomComputerPlayer('X'), SmartComputerPlayer('O'))
    else:
        print("Smart Computer(X) vs Smart Computer(O) Game starts ...\n")
        play(TicTacToe(), SmartComputerPlayer('X'), SmartComputerPlayer('O'))
