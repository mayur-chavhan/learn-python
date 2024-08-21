#!/usr/bin/env python3

def check_for_tie(board):
    return all(0 not in row for row in board)


def check_for_winner(player, board):
    # Diagonal
    # This is placed up here first because this runs
    # slightly quicker than the one in the for loop.
    if board[0][0] == board[1][1] == board[2][2] == player or \
            board[2][0] == board[1][1] == board[0][2] == player:
        return True

    return any(
        board[x][0] == board[x][1] == board[x][2] == player
        or board[0][x] == board[1][x] == board[2][x] == player
        for x in range(3)
    )


def create_playing_board():
    return [[0 for x in range(3)] for y in range(3)]


def play_game(board=None, player=1, turn=1):
    if board is None:
        print("Welcome to tic tac toe")                     # Preamble to starting the game...
        board = create_playing_board()

    print_current_board(board)
    board = play_turn(player, board)

    is_win = check_for_winner(player, board)                # Checks for a winner

    # Option 1  (don't use both options...)
    tied = check_for_tie(board)                             # Checks for tie

    # Option 2  (don't use both options...)
    tied = turn == 9 and not is_win

    # If there is a winner or tie...
    if is_win or tied:
        print_result(board, player, tied)                   # Declare winner / tie
        restart_game()
        return          # You must return out of this method,
                        # or the game will continue in infinite loop.

    # The game continues.
    player = (player % 2) + 1                               # Switch player
    play_game(board, player, turn + 1)                      # Call this method again.


# def set_marker(player, board):                            # Instead of this name,
def play_turn(player, board):                               # this name makes more sense.
    print("Player", player, " - x/y input between 0 and 2")

    x = y = 3

    while x not in range(3):    # Redundant parenthesis
        x = int(input("x: "))   # Casting to int
    while y not in range(3):    #
        y = int(input("y: "))   #

    if board[x][y] == 0:
        board[x][y] = player
    else:
        print('\nfield already used - choose again!')
        play_turn(player, board)

    return board


def print_current_board(board):
    print()
    print("   Y")
    print(" 2 |  ", board[0][2], '|', board[1][2], '|', board[2][2])
    print("   |   --+---+--")
    print(" 1 |  ", board[0][1], '|', board[1][1], '|', board[2][1])
    print("   |   --+---+--")
    print(" 0 |  ", board[0][0], '|', board[1][0], '|', board[2][0])
    print("      --------------- X")
    print("       0   1   2")
    print()


def print_result(board, player, tie):
    if tie:
        print("\n### It's a TIE! ###")
    elif player in [1, 2]:
        print("\n### Player {0} wins! ###".format(player))
    print_current_board(board)


def restart_game():
    # Ask the user if they are interested in playing again.
    print("\ndo you guys want to play again?")
    if int(input("0 = yes // 1 = no: ")):                   # If the user does not want to play again.
        return                                              # Leave this method.

    # Otherwise, restart the game.
    print("\n" + "*" * 15 + "\n" + "*" * 15 + "\n")         # "Block off" the previous game.
    print("Restarting the game...")                         # The preamble to restarting the game.
    play_game()


if __name__ == '__main__':
    play_game()
