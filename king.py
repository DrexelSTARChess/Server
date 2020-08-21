from chessPiece import ChessPiece


class King(ChessPiece):
    """docstring for King"""

    def __init__(self, color, i, j):
        super(King, self).__init__(color, i, j)
        self.rep = "K"

    def getPossibleMoves(self, board):
        print("Havn't done king possible moves yet!")
        return []
