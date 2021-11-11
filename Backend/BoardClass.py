from SpaceClass import *
from PieceClass import *
from PieceCatalogue import *
from SpaceIDsSingleton import *

# class that will represent the board of the game
class Board():
    # initializing the board
    def __init__(self):
        # dictionary to represent the physical board
        self.grid = {}
        # Piece Catalogue to hold all of the boards pieces
        self.pieces = PieceCatalogue()
        # building a new board
        self.buildNewBoard()
        # occupying the board with pieces
        self.occupyBoard()

    # function to build a new board
    def buildNewBoard(self):
        # running through the list of space IDs to fill the grid dictionary
        for id in spaceIDsSingleton.layout:
            for x in id:
                newSpace = Space(x)
                self.grid[x] = newSpace
                # flipping the color of the space
                if x in spaceIDsSingleton.lightSpaceIDs:
                    self.grid[x].color = 'light'
                elif x in spaceIDsSingleton.darkSpaceIDs:
                    self.grid[x].color = 'dark'

    # function to occupy a board with fresh pieces
    def occupyBoard(self):
        # occupying the board with the starting position of light pieces
        self.grid['a1'].piece = self.pieces.pieceList['rook1L']
        self.grid['b1'].piece = self.pieces.pieceList['knight1L']
        self.grid['c1'].piece = self.pieces.pieceList['bishop1L']
        self.grid['d1'].piece = self.pieces.pieceList['queenL']
        self.grid['e1'].piece = self.pieces.pieceList['kingL']
        self.grid['f1'].piece = self.pieces.pieceList['bishop2L']
        self.grid['g1'].piece = self.pieces.pieceList['knight2L']
        self.grid['h1'].piece = self.pieces.pieceList['rook2L']
        self.grid['a2'].piece = self.pieces.pieceList['pawn1L']
        self.grid['b2'].piece = self.pieces.pieceList['pawn2L']
        self.grid['c2'].piece = self.pieces.pieceList['pawn3L']
        self.grid['d2'].piece = self.pieces.pieceList['pawn4L']
        self.grid['e2'].piece = self.pieces.pieceList['pawn5L']
        self.grid['f2'].piece = self.pieces.pieceList['pawn6L']
        self.grid['g2'].piece = self.pieces.pieceList['pawn7L']
        self.grid['h2'].piece = self.pieces.pieceList['pawn8L']
        # occupying the board with the starting position of the dark pieces
        self.grid['a8'].piece = self.pieces.pieceList['rook1D']
        self.grid['b8'].piece = self.pieces.pieceList['knight1D']
        self.grid['c8'].piece = self.pieces.pieceList['bishop1D']
        self.grid['d8'].piece = self.pieces.pieceList['queenD']
        self.grid['e8'].piece = self.pieces.pieceList['kingD']
        self.grid['f8'].piece = self.pieces.pieceList['bishop2D']
        self.grid['g8'].piece = self.pieces.pieceList['knight2D']
        self.grid['h8'].piece = self.pieces.pieceList['rook2D']
        self.grid['a7'].piece = self.pieces.pieceList['pawn1D']
        self.grid['b7'].piece = self.pieces.pieceList['pawn2D']
        self.grid['c7'].piece = self.pieces.pieceList['pawn3D']
        self.grid['d7'].piece = self.pieces.pieceList['pawn4D']
        self.grid['e7'].piece = self.pieces.pieceList['pawn5D']
        self.grid['f7'].piece = self.pieces.pieceList['pawn6D']
        self.grid['g7'].piece = self.pieces.pieceList['pawn7D']
        self.grid['h7'].piece = self.pieces.pieceList['pawn8D']
        # marking the starting spots as occupied
        for id in spaceIDsSingleton.startingIDs:
            self.grid[id].occupied = True

    # function to display the board in the terminal
    def dispBoardTerm(self):
        count = 1
        print("----------------------------------------")
        for id in spaceIDsSingleton.layout:
            for x in id:
                if self.grid[x].occupied:
                    print("| "+self.grid[x].piece.label+" |", end='')
                else: 
                    print("|   |",end='')
                if count%8 == 0:
                    print('')
                    print("----------------------------------------")
                    count = 1
                else:
                    count+=1

    # function to move pieces with terminal for testing
    def movePieceTerm(self):
        # selecting the piece to be moved
        piece = input("Select a position to move: ")
        if self.grid[piece].occupied:
            # finding the available spaces for the piece
            self.grid[piece].findAvailable()
            # getting the new position for the piece
            newPos = input("Enter a new position: ")
            if newPos in self.grid[piece].piece.availableSpaces:
                # moving the piece to the new space
                self.grid[piece].piece.currentSpace = newPos
                self.grid[newPos].piece = self.grid[piece].piece
                self.grid[newPos].occupied = True
                self.grid[piece].piece = ''
                self.grid[piece].occupied = False
                self.grid[newPos].piece.availableSpaces.clear()
            else:
                print("Invalid move!")
        else:
            print("Invalid piece selected!")

if __name__ == '__main__':
    board = Board()
    print(board.grid['a1'].type)