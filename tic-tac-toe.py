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
        
        pawn = input("\n Do you want to play as 'X' or 'O: ").upper()
                
        if pawn == 'X':
            return {'X','O'}
        return {'O','X'}
    
def place_marker(Theboard, position, player):
    
    Theboard[position] = player
    
    
def check_for_winner(board, player1):

    return ((board[7] == player1 and board[8] == player1 and board[9] == player1) or 
            (board[4] == player1 and board[5] == player1 and board[6] == player1) or
            (board[1] == player1 and board[2] == player1 and board[3] == player1) or
            (board[7] == player1 and board[4] == player1 and board[1] == player1) or
            (board[8] == player1 and board[5] == player1 and board[2] == player1) or
            (board[9] == player1 and board[6] == player1 and board[3] == player1) or
            (board[7] == player1 and board[5] == player1 and board[3] == player1) or
            (board[1] == player1 and board[5] == player1 and board[9] == player1) or
            (board[9] == player1 and board[5] == player1 and board[1] == player1))
    # board_range = range(1,9)
    # for i in board_range:
    #     return board[i] == board[i] == board[i] == player
    
def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    return board[position] == ' '

def full_board(board):
    
    return not any(space_check(board, i) for i in range(1,9))

def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("\n Enter a digit [1-9] for position: "))
        
        return position
    
def replay():
    
    choice = input("\n Do you want to play again? [y/n] : ")
    
    if choice in {'Yes','y','yup'}:
        return True
    else:
        exit()
        
while True:
    
    theBoard = [' '] * 10
    
    player1, player2 = player_input()
    
    turn = choose_first()
    
    print("\n",turn, "Will go first")
    
    play_game = input("\n Do you want to play ? [y/n]: ")
          
    game_on = play_game.lower()[0] == 'y'
            
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, position, player1)
            
            
            if check_for_winner(theBoard, player1):
                display_board(theBoard)
                print("\n You have WON!!")
                game_on = False
            elif full_board(theBoard):
                display_board(theBoard)
                print("\n The Game is Draw!!")
            else:
                turn = 'Player 2'
        else:
                        
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, position, player2)
                
            if check_for_winner(theBoard, player2):
                display_board(theBoard)
                print("\n Player 2 has WON!!")
                game_on = False
            elif full_board(theBoard):
                display_board(theBoard)
                print("\n The Game is Tie!!")
            else:
                turn = 'Player 1'
                
    if not replay():
        break
    
                
                
                
                
    
# tic_board = [' '] * 10
# display_board(tic_board)
# check_for_winner(tic_board, 'X')