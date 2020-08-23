from chessPiece import ChessPiece


class Bishop(ChessPiece):
    """docstring for Bishop"""

    def __init__(self, color, i, j):
        super(Bishop, self).__init__(color, i, j)
        self.rep = "B"
        self.name = "Bishop"

    def get_possible_moves(self, board):
        return self.get_diagonals(board)
