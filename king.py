from chessPiece import ChessPiece


class King(ChessPiece):
    """docstring for King"""

    def __init__(self, color, i, j):
        super(King, self).__init__(color, i, j)
        self.rep = "K"
        self.name = "King"
        self.can_castle = True

    def get_possible_moves(self, board):
        return self.get_king_moves(board) + self.castle(board)

    def castle(self, board):

        castle_moves = []
        if self.color == "white":
            if self.can_castle and\
                    board[self.i][self.j + 1] == "noPiece" and\
                    board[self.i][self.j + 2] == "noPiece" and\
                    board[self.i][self.j + 3] != "noPiece" and\
                    board[self.i][self.j + 3].rep == "R" and\
                    board[self.i][self.j + 3].can_castle:
                move = "c%d,%d" % (10, 10)
                castle_moves.append(move)
            if self.can_castle and\
                    board[self.i][self.j - 1] == "noPiece" and\
                    board[self.i][self.j - 2] == "noPiece" and\
                    board[self.i][self.j - 3] == "noPiece" and\
                    board[self.i][self.j - 4] != "noPiece" and\
                    board[self.i][self.j - 4].rep == "R" and\
                    board[self.i][self.j - 4].can_castle:
                move = "c%d,%d" % (10, -10)
                castle_moves.append(move)
        else:
            if self.can_castle and\
                    board[self.i][self.j + 1] == "noPiece" and\
                    board[self.i][self.j + 2] == "noPiece" and\
                    board[self.i][self.j + 3] != "noPiece" and\
                    board[self.i][self.j + 3].rep == "R" and\
                    board[self.i][self.j + 3].can_castle:
                move = "c%d,%d" % (10, 10)
                castle_moves.append(move)
            if self.can_castle and\
                    board[self.i][self.j - 1] == "noPiece" and\
                    board[self.i][self.j - 2] == "noPiece" and\
                    board[self.i][self.j - 3] == "noPiece" and\
                    board[self.i][self.j - 4] != "noPiece" and\
                    board[self.i][self.j - 4].rep == "R" and\
                    board[self.i][self.j - 4].can_castle:
                move = "c%d,%d" % (10, -10)
                castle_moves.append(move)

        return castle_moves
