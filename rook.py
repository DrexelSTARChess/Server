from chessPiece import ChessPiece


class Rook(ChessPiece):
    """docstring for Rook"""

    def __init__(self, color, i, j):
        super(Rook, self).__init__(color, i, j)
        self.rep = "R"

    def getPossibleMoves(self, board):
        return self.getCardinals(board)
