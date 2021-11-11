from BoardClass import *
from SpaceIDsSingleton import *

board = Board()
board.dispBoardTerm()
while(True):
    board.movePieceTerm()
    board.dispBoardTerm()