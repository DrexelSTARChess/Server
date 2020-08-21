from chessPiece import ChessPiece


class Queen(ChessPiece):
    """docstring for Queen"""

    def __init__(self, color, i, j):
        super(Queen, self).__init__(color, i, j)
        self.rep = "Q"

    def getPossibleMoves(self, board):
        """I'm gonna try out this crazy queen algorithm, if i get it to work, it will be wayy more efficient that like 8 loops lmao"""
        return self.getCardinals(board) + self.getDiagnals(board)
