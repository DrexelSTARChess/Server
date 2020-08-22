from chessPiece import ChessPiece


class Rook(ChessPiece):
    """docstring for Rook"""

    def __init__(self, color, i, j):
        super(Rook, self).__init__(color, i, j)
        self.rep = "R"
        self.canCastle = True
        self.name = "Rook"

    def getPossibleMoves(self, board):
        if self.i != 0 or self.i != 7 or self.j != 0 or self.j != 7:
            self.canCastle = False

        return self.getCardinals(board)
