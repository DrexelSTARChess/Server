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
        self.enpassant = False
        self.name = "Pawn"

    def getPossibleMoves(self, board):

        possibleMoves = []
        #pawns are the only directionally oriented piece so this is the only one that should require explicit white/black checks for direction
        #start by searching if square directly infront is empty

        #just add pawn promotion now

        #if its white, add 1 to the y value, else subtract 1, have a bounds check
        movementFactor = 0
        if self.color == "white":
            movementFactor = -1
        else:
            movementFactor = 1

        if self.isBoundedSquare(self.i + (movementFactor * 2), self.j) and board[self.i + (movementFactor * 2)][self.j] == "noPiece" and self.notMoved:
            move = "%d,%d" % (self.i + (movementFactor*2), self.j)
            # print("triggered for", self.color)
            possibleMoves.append(move)
        if self.isBoundedSquare(self.i + movementFactor, self.j) and board[self.i + movementFactor][self.j] == "noPiece":
            move = "%d,%d" % (self.i + movementFactor, self.j)
            possibleMoves.append(move)
        if self.isBoundedSquare(self.i + movementFactor, self.j - 1) and board[self.i + movementFactor][self.j - 1] != "noPiece" and board[self.i + movementFactor][self.j - 1].getColor() != self.color:
            move = "x%d,%d" % (self.i + movementFactor, self.j - 1)
            possibleMoves.append(move)
        if self.isBoundedSquare(self.i + movementFactor, self.j + 1) and board[self.i + movementFactor][self.j + 1] != "noPiece" and board[self.i + movementFactor][self.j + 1].getColor() != self.color:
            move = "x%d,%d" % (self.i + movementFactor, self.j + 1)
            possibleMoves.append(move)
        if self.isBoundedSquare(self.i + movementFactor, self.j - 1) and board[self.i + movementFactor][self.j - 1] == "noPiece" and board[self.i][self.j - 1] != "noPiece" and board[self.i][self.j - 1].color != self.color and board[self.i][self.j - 1].rep == "P" \
                and board[self.i][self.j - 1].enpassant:
            move = "x%d,%d" % (self.i + movementFactor, self.j - 1)
            possibleMoves.append(move)
            # print("ALETR")
        if self.isBoundedSquare(self.i + movementFactor, self.j + 1) and board[self.i + movementFactor][self.j + 1] == "noPiece" and board[self.i][self.j + 1] != "noPiece" and board[self.i][self.j + 1].color != self.color and board[self.i][self.j + 1].rep == "P" \
                and board[self.i][self.j + 1].enpassant:
            move = "x%d,%d" % (self.i + movementFactor, self.j + 1)
            possibleMoves.append(move)
            # print("ALETR2")

        return possibleMoves
