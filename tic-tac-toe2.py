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
    
    choice = ' '
        
    while choice not in {'X','O'}:
        
        choice = input("\n Do you want to play as 'X' or 'O': ").upper()
        
        if choice == 'X':
            return {'X','O'}
        else:
            return {'O','X'}
        
def who_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def check_win(board, player1):
    
    return ((board[7] == board[8] == board[9] == player1) or 
            (board[4] == board[5] == board[6] == player1) or
            (board[1] == board[2] == board[3] == player1) or
            (board[7] == board[4] == board[1] == player1) or
            (board[8] == board[5] == board[2] == player1) or
            (board[9] == board[6] == board[3] == player1) or
            (board[7] == board[5] == board[3] == player1) or
            (board[1] == board[5] == board[9] == player1) or
            (board[9] == board[5] == board[1] == player1))
    
def place_marker(theBoard, position, player1):
    
    theBoard[position] = player1
    

def space_check(theBoard, position):
    
    return theBoard[position] == ' '

def full_board(theBoard):
    
    return not any(space_check(theBoard, i) for i in range(1,10))

def player_choice(board):
    
    position = 0
    
    while position not in range(1,9) or space_check(board, position):
        position = int(input("\nEnter a digit [1 to 9] : "))
        return position
    
def replay():
    
        playing = input("\nDo you want to play again? [y/n]: ")

        return playing in {'y','yes','Yes','YES'}
    
    
while True:
    
    theBoard = [' '] * 10
    
    player1, player2 = player_input()
    
    turn = who_first()
    
    print("\n",turn," is going first")
    
    game_on = input("\nDo you want to begin the game? [y/n]: ")
    
    game_on = game_on.lower()[0] == 'y'
    
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(theBoard)
            
            position = player_choice(theBoard)
            
            place_marker(theBoard, position, player1)
            
            if check_win(theBoard, player1):
                display_board(theBoard)
                print("\nYou've WON!!")
                game_on = False
            elif full_board(theBoard):
                display_board(theBoard)
                print("\nThe Game is Draw!!")
            else:
                turn = 'Player 2'
        else:
            
            display_board(theBoard)
            
            position = player_choice(theBoard)
            
            place_marker(theBoard, position, player2)
            
            if check_win(theBoard, player2):
                display_board(theBoard)
                print("\nPlayer 2 has WON!!")
                game_on = False
            elif full_board(theBoard):
                display_board(theBoard)
                print("\nThe Game is Draw!!")
            else:
                turn = 'Player 1'
    if not replay():
        break
    
    
