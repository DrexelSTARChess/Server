from chessPiece import ChessPiece


class Knight(ChessPiece):
    """docstring for Knight"""

    def __init__(self, color, i, j):
        super(Knight, self).__init__(color, i, j)
        self.rep = "N"

    def getPossibleMoves(self, board):
        return self.getKnightMoves(board)
