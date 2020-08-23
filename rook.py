from chessPiece import ChessPiece


class Rook(ChessPiece):
    """docstring for Rook"""

    def __init__(self, color, i, j):
        super(Rook, self).__init__(color, i, j)
        self.rep = "R"
        self.can_castle = True
        self.name = "Rook"

    def get_possible_moves(self, board):
        if self.i != 0 or self.i != 7 or self.j != 0 or self.j != 7:
            self.can_castle = False

        return self.get_cardinals(board)
