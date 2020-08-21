from chessPiece import ChessPiece
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King


class Pawn(ChessPiece):
    """docstring for Pawn"""

    def __init__(self, color, i, j):
        super(Pawn, self).__init__(color, i, j)
        self.rep = "P"
        self.notMoved = True

    def getPossibleMoves(self, board):

        possibleMoves = []
        #pawns are the only directionally oriented piece so this is the only one that should require explicit white/black checks for direction
        #start by searching if square directly infront is empty

        #just add pawn promotion now

        #if its white, add 1 to the y value, else subtract 1, have a bounds check
        movementFactor = 0
        if self.color == "white":
            movementFactor = 1
        else:
            movementFactor = -1

        if board[self.i + movementFactor][self.j] == "noPiece" and self.isBoundedSquare(self.i + movementFactor, self.j) and self.notMoved:
            move = "%d,%d" % (self.i + (movementFactor*2), self.j)
            self.notMoved = False
            possibleMoves.append(move)
        if board[self.i + movementFactor][self.j] == "noPiece" and self.isBoundedSquare(self.i + movementFactor, self.j):
            move = "%d,%d" % (self.i + movementFactor, self.j)
            self.notMoved = False
            possibleMoves.append(move)
        if self.isBoundedSquare(self.i + movementFactor, self.j - 1) and board[self.i + movementFactor][self.j - 1] != "noPiece" and board[self.i + movementFactor][self.j - 1].getColor() != self.color:
            move = "x%d,%d" % (self.i + movementFactor, self.j - 1)
            self.notMoved = False
            possibleMoves.append(move)
        if self.isBoundedSquare(self.i + movementFactor, self.j + 1) and board[self.i + movementFactor][self.j + 1] != "noPiece" and board[self.i + movementFactor][self.j + 1].getColor() != self.color:
            move = "x%d,%d" % (self.i + movementFactor, self.j + 1)
            self.notMoved = False
            possibleMoves.append(move)

        """implement pawn promotion here by returning a new piece type"""


        return possibleMoves

