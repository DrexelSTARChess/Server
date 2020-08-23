from chessPiece import ChessPiece


class Queen(ChessPiece):
    """docstring for Queen"""

    def __init__(self, color, i, j):
        super(Queen, self).__init__(color, i, j)
        self.rep = "Q"
        self.name = "Queen"

    def get_possible_moves(self, board):
        return self.get_cardinals(board) + self.get_diagonals(board)
