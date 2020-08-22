from chessPiece import ChessPiece


class King(ChessPiece):
    """docstring for King"""

    def __init__(self, color, i, j):
        super(King, self).__init__(color, i, j)
        self.rep = "K"
        self.name = "King"
        self.canCastle = True

    def getPossibleMoves(self, board):
        return self.getKingMoves(board) + self.castle(board)

    def castle(self, board):

        castleMoves = []
        if self.color == "white":
            if self.canCastle and board[self.i][self.j + 1] == "noPiece" and board[self.i][self.j + 2] == "noPiece" and \
                            board[self.i][self.j + 3] != "noPiece" and board[self.i][self.j + 3].rep == "R" and \
                    board[self.i][self.j + 3].canCastle:
                move = "c%d,%d" % (10, 10)
                castleMoves.append(move)
            if self.canCastle and board[self.i][self.j - 1] == "noPiece" and board[self.i][self.j - 2] == "noPiece" and \
                            board[self.i][self.j - 3] == "noPiece" and board[self.i][self.j - 4] != "noPiece" and \
                            board[self.i][self.j - 4].rep == "R" and \
                    board[self.i][self.j - 4].canCastle:
                move = "c%d,%d" % (10, -10)
                castleMoves.append(move)
        else:
            if self.canCastle and board[self.i][self.j + 1] == "noPiece" and board[self.i][self.j + 2] == "noPiece" and \
                            board[self.i][self.j + 3] != "noPiece" and board[self.i][self.j + 3].rep == "R" and \
                    board[self.i][self.j + 3].canCastle:
                move = "c%d,%d" % (10, 10)
                castleMoves.append(move)
            if self.canCastle and board[self.i][self.j - 1] == "noPiece" and board[self.i][self.j - 2] == "noPiece" and \
                            board[self.i][self.j - 3] == "noPiece" and board[self.i][self.j - 4] != "noPiece" and \
                            board[self.i][self.j - 4].rep == "R" and \
                    board[self.i][self.j - 4].canCastle:
                move = "c%d,%d" % (10, -10)
                castleMoves.append(move)

        return castleMoves
