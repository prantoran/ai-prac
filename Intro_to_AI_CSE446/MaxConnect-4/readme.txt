Name  	      : Pinku Deb Nath, 
NSU ID	      : 1310610042, 
assignment no : 2 


The minimax function, maxvalue function,
minValue function and the evaluation functions
are implemented in the same maxConnect4Game.py 
file where the class maxConnect4Game is present
so that implementation and usage of global
variables are simpler. I have implemented
1. minimax
2. alpha-beta pruning
3. depth-limited version of minimax with evaluation function
The code was originally written in pyhton 2.7 
but it is upgraded to python 3.5, so
python 3.5 is needed to run the code. Little to no changes
are made to the original maxConnect4.py and maxConnect4game.py
files and the maxConnect4Game class. However, the function
playPiece() is modified to return row number used to make a move.
This is used for optimization purposes.
The program works perfectly for depth 7, however the time required
to terminate increases for higher depths.

The code runs in the same way as mentioned in the assigment. 
The same command line instructions work both in Windows 
cmd command line terminal and Linux terminal, provided 
that python 3.5 is installed and running.
The formats are:
python maxconnect4 one-move [input_file] [output_file] [depth]
eg. python maxconnect4 one-move red_next.txt green_next.txt 5 or
python maxconnect4 interactive [input_file] [computer-next/human-next] [depth]
eg. python maxconnect4.py interactive input1.txt computer-next 7 

