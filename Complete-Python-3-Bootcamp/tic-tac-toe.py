#!/usr/bin/env python3

from IPython.display import clear_output
import random

def display_board(board):

    clear_output()

    print("\n\t -----------")
    print('\t|',board[7],'|',board[8],'|',board[9],'|')
    print("\t|---|---|---|")
    print('\t|',board[4],'|',board[5],'|',board[6],'|')
    print("\t|---|---|---|")
    print('\t|',board[1],'|',board[2],'|',board[3],'|')
    print("\t -----------\n")


def player_input():

    pawn = ''

    while pawn not in {'X', 'O'}:

        pawn = input("\n\t  Do you want to play as 'X' or 'O': ").upper()

        if pawn == 'X':
            return ('X','O')
        else:
            return ('O','X')


def place_marker(board, pawn, position):
    
    board[position] = pawn
    

def win_check(board, player1):
    '''
    Checking in Horizontal, Vertical and Diagonal for player's marker if WON 
    '''
    return ((board[7] == board[8] == board[9] == player1) or 
            (board[4] == board[5] == board[6] == player1) or
            (board[1] == board[2] == board[3] == player1) or
            (board[7] == board[4] == board[1] == player1) or
            (board[8] == board[5] == board[2] == player1) or
            (board[9] == board[6] == board[3] == player1) or
            (board[7] == board[5] == board[3] == player1) or
            (board[1] == board[5] == board[9] == player1) or
            (board[9] == board[5] == board[1] == player1))


def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'
    
def space_check(board, position):
    return board[position] == ' '
        
        
def full_board_check(board):
    
    return not any(space_check(board,i) for i in range(1,10))

def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a position [1 to 9]: "))
        
    return position

def replay():
    
    choice = input("\n\n\tPlay again?? Enter Yes or No : ")

    if choice in {'yes','y','Yes','YES'}:
        return choice
    print("\n\tByeee!! \n\n")
    exit()


# While loop to keep running the game

print("\n\t ==============[X]==================")
print("\n\t   Welcome to Tic-Tac-Toe Game!!")
print("\n\t ==============[O]==================")

while True:
    # Reset the board
    theBoard = [' '] * 10 
    ''' The Board is filled with empty spaces for 10 times in list
        For example theBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    '''
    player1_marker, player2_marker = player_input() # player_input function's output is split into two player markers to determine who's X and who's O
    turn = choose_first()       # choose_first function will randomize who will go first in turn variable
    print("\n\t ==>",turn,' will go first.\n')

    print("\n\t ===================================================")
    play_game = input('\n\tAre you ready to play? Enter Yes or No: ')
    print("\n\t ===================================================")

    game_on = play_game.lower()[0] == 'y'
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('\n\tCongratulations! You have won the game!')
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print('\n\tThe Game is Draw!')
                break
            else:
                turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('\n\tPlayer 2 has won!')
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print('\n\tThe game is a draw!')
                break
            else:
                turn = 'Player 1'
# below if condition tells if it's false then it will break out of the loop.
    if not replay():
        break
