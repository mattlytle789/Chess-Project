from SpaceIDsSingleton import *

import numpy as np

# class that will represent a singular space on the board
class Space():
    # initializing the space class
    def __init__(self, id):
        self.color = ''
        self.occupied = False
        self.piece = None
        self.ID = id
    
    # function to find available spaces to move a piece to
    def findAvailable(self):
        # if the current space is not occupied return immediately 
        if not self.occupied:
            return 

        # getting the indices of the current space ID in the list of space IDs
        yPos = np.asarray(np.where(spaceIDsSingleton.layout == self.ID)).T[0][0]
        xPos = np.asarray(np.where(spaceIDsSingleton.layout == self.ID)).T[0][1]

        # option for if the current piece is a pawn
        if self.piece.type == 'pawn':
            # checking if the pawn has moved already
            if not self.piece.hasMoved:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-1,xPos])
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-2,xPos])
            else:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-1,xPos])
            # checking if the space diagonal to the pawn is occupied by an opposing piece
        # option for if the current piece is a rook
        elif self.piece.type == 'rook':
            # rook is able to move as many spaces forward until an occupied space
            index = 1+yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-i,xPos])
            # rook is able to move as many spaces backwards until an occupied space
            index = 8-yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+i,xPos])
            # rook is able to move as many spaces right until an occupied space
            index = 8-xPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos,xPos+i])
            # rook is able to move as many spaces left until occupied space
            index = 1+xPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos,xPos-i])
        # option for if the current piece is a knight
        elif self.piece.type == 'knight':
            # knight can move forward 2 and right 1
            if yPos-2>=0 and xPos+1<8:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-2,xPos+1])
            # knight can move forward 2 and left 1
            if yPos-2>=0 and xPos-1>=0:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-2,xPos-1])
            # knight can move forward 1 and right 2
            if yPos-1>=0 and xPos+2<8:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-1,xPos+2])
            # knight can move forward 1 and left 2
            if yPos-1>=0 and xPos-2>=0:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-1,xPos-2])
            # knight can move backward 2 and right 1
            if yPos+2<8 and xPos+1<8:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+2,xPos+1])
            # knight can move backward 2 and left 1
            if yPos+2<8 and xPos-1>=0:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+2,xPos-1])
            # knight can move backward 1 and right 2
            if yPos+1<8 and xPos+2<8:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+1,xPos+2])
            # knight can move backward 1 and left 2
            if yPos+1<8 and xPos-2>=0:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+1,xPos-2]) 
        # option for if the current piece is a bishop
        elif self.piece.type == 'bishop':
            # bishop is able to move forward and right diagonlly
            if 8-xPos<1+yPos:
                index = 8-xPos
            else:
                index = 1+yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-i,xPos+i])
            # bishop is able to move forward and left diagonally 
            if 1+xPos<1+yPos:
                index = 1+xPos
            else:
                index = 1+yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-i,xPos-i])
            # bishop is able to move backward and right diagonally
            if 8-xPos<8-yPos:
                index = 8-xPos
            else:
                index = 8-yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+i,xPos+i])
            # bishop is able to move backward and left diagonally 
            if 1+xPos<8-yPos:
                index = 1+xPos
            else:
                index = 8-yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+i,xPos-i])
        # option for if the current piece is a queen
        elif self.piece.type == 'queen':
            # queen is able to move as many spaces forward until an occupied space
            index = 1+yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-i,xPos])
            # queen is able to move as many spaces backwards until an occupied space
            index = 8-yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+i,xPos])
            # queen is able to move as many spaces right until an occupied space
            index = 8-xPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos,xPos+i])
            # queen is able to move as many spaces left until occupied space
            index = 1+xPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos,xPos-i])
            # queen is able to move forward and right diagonlly
            if 8-xPos<1+yPos:
                index = 8-xPos
            else:
                index = 1+yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-i,xPos+i])
            # queen is able to move forward and left diagonally 
            if 1+xPos<1+yPos:
                index = 1+xPos
            else:
                index = 1+yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-i,xPos-i])
            # queen is able to move backward and right diagonally
            if 8-xPos<8-yPos:
                index = 8-xPos
            else:
                index = 8-yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+i,xPos+i])
            # queen is able to move backward and left diagonally 
            if 1+xPos<8-yPos:
                index = 1+xPos
            else:
                index = 8-yPos
            for i in range(1,index):
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+i,xPos-i])
        # option for if the current piece is a king 
        elif self.piece.type == 'king':
            # king is able to move forward one space
            if yPos-1>=0:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-1,xPos])
            # king is able to move backward one space
            if yPos+1<8:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+1,xPos])
            # king is able to move right one space
            if xPos+1<8:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos,xPos+1])
            # king is able to move left one space
            if xPos-1>=0:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos,xPos-1])
            # king is able to move forward and right diagonally
            if yPos-1>=0 and xPos+1<8:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-1,xPos+1])
            # king is able to move forward and left diagonally
            if yPos-1>=0 and xPos-1>=0:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos-1,xPos-1])
            # king is able to move backward and right diagonally
            if yPos+1<8 and xPos+1<8:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+1,xPos+1])
            # king is able to move backward and left diagonally
            if yPos+1<8 and xPos-1>=0:
                self.piece.availableSpaces.append(spaceIDsSingleton.layout[yPos+1,xPos-1])

        print("Available Spaces:",end=' ')
        print(self.piece.availableSpaces)