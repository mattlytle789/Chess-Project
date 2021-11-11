from PieceClass import *

# class that will hold all of the pieces 
class PieceCatalogue():
    #initializing the catalogue
    def __init__(self):
        # creating a dictionary to hold all of the pieces
        self.pieceList = {}
        # creating all of the light pieces and adding them to the dictionary
        self.pawn1L = Piece('a2', 'pawn', 'light', 'P')
        self.pawn2L = Piece('b2', 'pawn', 'light', 'P')
        self.pawn3L = Piece('c2', 'pawn', 'light', 'P')
        self.pawn4L = Piece('d2', 'pawn', 'light', 'P')
        self.pawn5L = Piece('e2', 'pawn', 'light', 'P')
        self.pawn6L = Piece('f2', 'pawn', 'light', 'P')
        self.pawn7L = Piece('g2', 'pawn', 'light', 'P')
        self.pawn8L = Piece('h2', 'pawn', 'light', 'P')
        self.rook1L = Piece('a1', 'rook', 'light', 'R')
        self.rook2L = Piece('h1', 'rook', 'light', 'R')
        self.knight1L = Piece('b1', 'knight', 'light', 'H')
        self.knight2L = Piece('g1', 'knight', 'light', 'H')
        self.bishop1L = Piece('c1', 'bishop', 'light', 'B')
        self.bishop2L = Piece('f1', 'bishop', 'light', 'B')
        self.queenL = Piece('d1', 'queen', 'light', 'Q')
        self.kingL = Piece('e1', 'king', 'light', 'K')
        self.pieceList['pawn1L'] = self.pawn1L
        self.pieceList['pawn2L'] = self.pawn2L
        self.pieceList['pawn3L'] = self.pawn3L
        self.pieceList['pawn4L'] = self.pawn4L
        self.pieceList['pawn5L'] = self.pawn5L
        self.pieceList['pawn6L'] = self.pawn6L
        self.pieceList['pawn7L'] = self.pawn7L
        self.pieceList['pawn8L'] = self.pawn8L
        self.pieceList['rook1L'] = self.rook1L
        self.pieceList['rook2L'] = self.rook2L
        self.pieceList['knight1L'] = self.knight1L
        self.pieceList['knight2L'] = self.knight2L
        self.pieceList['bishop1L'] = self.bishop1L
        self.pieceList['bishop2L'] = self.bishop2L
        self.pieceList['queenL'] = self.queenL
        self.pieceList['kingL'] = self.kingL
        # creating all of the dark pieces
        self.pawn1D = Piece('a7', 'pawn', 'dark', 'P')
        self.pawn2D = Piece('b7', 'pawn', 'dark', 'P')
        self.pawn3D = Piece('c7', 'pawn', 'dark', 'P')
        self.pawn4D = Piece('d7', 'pawn', 'dark', 'P')
        self.pawn5D = Piece('e7', 'pawn', 'dark', 'P')
        self.pawn6D = Piece('f7', 'pawn', 'dark', 'P')
        self.pawn7D = Piece('g7', 'pawn', 'dark', 'P')
        self.pawn8D = Piece('h7', 'pawn', 'dark', 'P')
        self.rook1D = Piece('a8', 'rook', 'dark', 'R')
        self.rook2D = Piece('h8', 'rook', 'dark', 'R')
        self.knight1D = Piece('b8', 'knight', 'dark', 'H')
        self.knight2D = Piece('g8', 'knight', 'dark', 'H')
        self.bishop1D = Piece('c8', 'bishop', 'dark', 'B')
        self.bishop2D = Piece('f8', 'bishop', 'dark', 'B')
        self.queenD = Piece('d8', 'queen', 'dark', 'Q')
        self.kingD = Piece('e8', 'king', 'dark', 'K')
        self.pieceList['pawn1D'] = self.pawn1D
        self.pieceList['pawn2D'] = self.pawn2D
        self.pieceList['pawn3D'] = self.pawn3D
        self.pieceList['pawn4D'] = self.pawn4D
        self.pieceList['pawn5D'] = self.pawn5D
        self.pieceList['pawn6D'] = self.pawn6D
        self.pieceList['pawn7D'] = self.pawn7D
        self.pieceList['pawn8D'] = self.pawn8D
        self.pieceList['rook1D'] = self.rook1D
        self.pieceList['rook2D'] = self.rook2D
        self.pieceList['knight1D'] = self.knight1D
        self.pieceList['knight2D'] = self.knight2D
        self.pieceList['bishop1D'] = self.bishop1D
        self.pieceList['bishop2D'] = self.bishop2D
        self.pieceList['queenD'] = self.queenD
        self.pieceList['kingD'] = self.kingD
