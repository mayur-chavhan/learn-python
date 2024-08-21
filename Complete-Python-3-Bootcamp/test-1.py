#!/usr/bin/env python3

game_list = ['0','1','2']

def display_game(game_list):
    print("\n\tHere's the Game display\n")
    
    print("\t",game_list,"\n")
    

def position_choice():
    
    choices = input("\n\tEnter a number to replace a position [0 to 2]: ")

    
    while choices not in game_list:
        
        choices = input("\n\tEnter a number to replace a position [0 to 2]: ")

        if choices not in game_list:
            print("\n\tEnter a number between 0 to 2:\n")
            
    return int(choices)

def replacement_choice(game_list,position):

    user_placement = input("\n\tType your string to place at position: ")
    
    game_list[position] = user_placement
    
    return game_list


def gameon_choice():
    choice = "Wrong"

    while choice not in ['y','n']:

        choice = input("\n\tKeep playing (y or n): ")

        if choice not in ['y','n']:
            print("\n\tSorry!! Invalid Choice!! Please choice y or n\n") 

    if choice == "y":
        return True
    print("\nBye!!!\n")
    exit(0)


game_on = True

while game_on:
    display_game(game_list)
    
    position = position_choice()
    
   # position = range(0,position - 1)
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()
    
# position_choice()
# replacement_choice(game_list,position)
# display_game(game_list)
