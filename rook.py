from chessPiece import ChessPiece


class Rook(ChessPiece):
    """docstring for Rook"""

    def __init__(self, color, i, j):
        super(Rook, self).__init__(color, i, j)
        self.rep = "R"
        self.can_castle = True
        self.name = "Rook"
        self.oi = i
        self.oj = j

    def get_possible_moves(self, board):
        if self.i != self.i or self.j != self.oj:
            self.can_castle = False

        return self.get_cardinals(board)
