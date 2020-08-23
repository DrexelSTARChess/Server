from chessPiece import ChessPiece


class Knight(ChessPiece):
    """docstring for Knight"""

    def __init__(self, color, i, j):
        super(Knight, self).__init__(color, i, j)
        self.rep = "N"
        self.name = "Knight"

    def get_possible_moves(self, board):
        return self.get_knight_moves(board)
