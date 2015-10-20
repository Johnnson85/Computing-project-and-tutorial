#tic tac toe board code



# Tic Tac Toe
  
import random
board=["x","x","o","o","o","x","o","o","x"] 
def drawBoard(board):
    
# This function prints out the board that it was passed.

# "board" is a list of 10 strings representing the board (ignore index 0)

    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print(drawBoard)

drawBoard(board)
    
