from chessPiece import ChessPiece


class Queen(ChessPiece):
    """docstring for Queen"""

    def __init__(self, color, i, j):
        super(Queen, self).__init__(color, i, j)
        self.rep = "Q"
        self.name = "Queen"

    def getPossibleMoves(self, board):
        return self.getCardinals(board) + self.getDiagnals(board)
