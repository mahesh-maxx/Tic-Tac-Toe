# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 23:56:47 2017

@author: mahes
"""
from display_board import display_board,player_input,place_marker,win_check,choose_first,full_board_check,player_choice,replay
print('Welcome to Tic Tac Toe Game')

while True:
    theBoard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    
    game_on = True
    print(turn + ' will play first')
    while game_on:
        if turn == 'Player 1':
            
            display_board(theBoard)
            print('Player 1 turn')
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 is won')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Oops! The Game is draw')
                    break
                else:
                    turn = 'Player 2'
        else:
            
            display_board(theBoard)
            print('Player 2 Turn')
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 is won')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Oops! The Game is draw')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
                    
                    
                