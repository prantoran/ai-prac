#!/usr/bin/env python

#Name  	       : Pinku Deb Nath, 
#NSU ID	       : 1310610042, 
#Assignment no : 2 


# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible  

import sys
from MaxConnect4Game import *


def oneMoveGame(currentGame,depth):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay(depth) # Make a move (only random is implemented)

    print ('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print(('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score)))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()



def interactiveGame(currentGame,curPlayer,depth):
    #moveRemaining is used to count the iterations left before termination of while loop
    moveRemaining=42 - currentGame.pieceCount
   
    while moveRemaining >=0:
        print ('Current Game state:')
        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: User = %d, Computer = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        
        if not moveRemaining:   #no more free spaces left
            break
        if curPlayer == 1:
            print("Turn for user to play, input the row number[1-6] and the column number [1-7]:")
            print("To exit the game, type 'exit confirmed' without quotes")
            currentGame.currentTurn=1
            invalid=1
            row=0
            col=0
            while invalid:          #valid position is yet to be found
                row,col=input().split()
                try:
                    row=int(row)
                    col=int(col)
                except ValueError:
                    if row=="exit" or row=="EXIT":
                        return
                    print("Input are not integers!")
                    print("Input two integers with space in between.")
                    print("To exit the game, type 'exit confirmed' without quotes")
                    continue
                print("row:",row,"col:",col)
                row-=1
                col-=1
                #checking whether there is space underneath the choice is empty
                if row==5 or ( row<5 and currentGame.gameBoard[row+1][col]):
                    #checking whether the chosen space is empty
                    if not currentGame.gameBoard[row][col]:
                        invalid=0
                    else:
                        print("The position(",row+1,",",col+1,") is filled, try another (row,col):")
    
                else:
                    print("The space underneath the position is not filled! Try another (row,col):")                    
            row=currentGame.playPiece(col)
            curPlayer=2

            try:
                currentGame.gameFile = open("human.txt", 'w')
            except:
                sys.exit('Error opening output file.')
            
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            
        else:
            currentGame.currentTurn=2
            currentGame.aiPlay(depth)
            curPlayer=1

            try:
                currentGame.gameFile = open("computer.txt", 'w')
            except:
                sys.exit('Error opening output file.')
            
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            
        moveRemaining-=1
    
    #sys.exit('Interactive mode is currently not implemented')


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print(('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0]))
        print(('or: %s one-move [input_file] [output_file] [depth]' % argv[0]))
        sys.exit(2)


    depth=argv[4]
    
    game_mode, inFile = argv[1:3]



    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    #Preprocessing for interactive
    curPlayer=1                     #1 stands for human in interactive
    if game_mode=='interactive' :
        if argv[3]=='computer-next':
            curPlayer=2
        

    
    #If input file does not exist then we are creating a file in initial 
    fin=None
    try:
        fin = open(inFile, 'r')
    except IOError:
        fin=open(inFile,'w')
        for row in range(6):
            fin.write(''.join("0" for col in range(7)) + '\r\n')
        fin.write('%d\r\n' % curPlayer)
        print(inFile,"do not exist but an empty file in initial state has been created")
    fin.close()

    print("curPlayer:",curPlayer)


    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        interactiveGame(currentGame,curPlayer,depth) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,depth) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



