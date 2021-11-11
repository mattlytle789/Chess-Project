import numpy as np

# singleton class that will hold all of the arrays of spaceIDs
class SpaceIDsSingleton:
    # initializing the arrays of space IDs
    def __init__(self):
        # list with the space ids in the proper layout
        self.layout = np.array([['a8','b8','c8','d8','e8','f8','g8','h8'],
                                ['a7','b7','c7','d7','e7','f7','g7','h7'],
                                ['a6','b6','c6','d6','e6','f6','g6','h6'],
                                ['a5','b5','c5','d5','e5','f5','g5','h5'],
                                ['a4','b4','c4','d4','e4','f4','g4','h4'],
                                ['a3','b3','c3','d3','e3','f3','g3','h3'],
                                ['a2','b2','c2','d2','e2','f2','g2','h2'],
                                ['a1','b1','c1','d1','e1','f1','g1','h1']])
        # list with the space IDs that are populated at the start of the game
        self.startingIDs = np.array(['a1','a2','a8','a7',
                                    'b1','b2','b8','b7',
                                    'c1','c2','c8','c7',
                                    'd1','d2','d8','d7',
                                    'e1','e2','e8','e7',
                                    'f1','f2','f8','f7',
                                    'g1','g2','g8','g7',
                                    'h1','h2','h8','h7'])
        # list to hold all possible space ids in order
        self.spaceIDs = np.array(['a1','a2','a3','a4','a5','a6','a7','a8',
                                'b1','b2','b3','b4','b5','b6','b7','b8',
                                'c1','c2','c3','c4','c5','c6','c7','c8',
                                'd1','d2','d3','d4','d5','d6','d7','d8',
                                'e1','e2','e3','e4','e5','e6','e7','e8',
                                'f1','f2','f3','f4','f5','f6','f7','f8',
                                'g1','g2','g3','g4','g5','g6','g7','g8',
                                'h1','h2','h3','h4','h5','h6','h7','h8'])
        # list with all light colored space IDs
        self.lightSpaceIDs = np.array(['b8','d8','f8','h8',
                                        'a7','c7','e7','g7',
                                        'b6','d6','f6','h6',
                                        'a5','c5','e5','g5',
                                        'b4','d4','f4','h4',
                                        'a3','c3','e3','g3',
                                        'b2','d2','f2','h2',
                                        'a1','c1','e1','g1'])
        # list with all dark colored space IDs
        self.darkSpaceIDs = np.array(['a8','c8','e8','g8',
                                        'b7','d7','f7','h7',
                                        'a6','c6','e6','g6',
                                        'b5','d5','f5','h5',
                                        'a4','c4','e4','g4',
                                        'b3','d3','f3','h3',
                                        'a2','c2','e2','g2',
                                        'b1','d1','f1','h1'])

spaceIDsSingleton = SpaceIDsSingleton()