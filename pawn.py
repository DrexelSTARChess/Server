from chessPiece import ChessPiece


class Pawn(ChessPiece):
    """docstring for Pawn"""

    def __init__(self, color, i, j):
        super(Pawn, self).__init__(color, i, j)
        self.rep = "P"
        self.notMoved = True
        self.enpassant = False
        self.name = "Pawn"

    def get_possible_moves(self, board):

        possible_moves = []

        # if its white, add 1 to the y value,
        # else subtract 1, have a bounds check
        movement_factor = 0
        if self.color == "white":
            movement_factor = -1
        else:
            movement_factor = 1

        if self.is_bounded_square(self.i + (movement_factor * 2), self.j) and\
                board[self.i + (movement_factor * 2)][self.j] == "noPiece" and\
                self.notMoved:
            move = "%d,%d" % (self.i + (movement_factor*2), self.j)
            # print("triggered for", self.color)
            possible_moves.append(move)
        if self.is_bounded_square(self.i + movement_factor, self.j) and\
                board[self.i + movement_factor][self.j] == "noPiece":
            move = "%d,%d" % (self.i + movement_factor, self.j)
            possible_moves.append(move)
        if self.is_bounded_square(self.i + movement_factor, self.j - 1) and\
                board[self.i + movement_factor][self.j - 1] != "noPiece" and\
                board[self.i + movement_factor][self.j - 1].get_color()\
                != self.color:
            move = "x%d,%d" % (self.i + movement_factor, self.j - 1)
            possible_moves.append(move)
        if self.is_bounded_square(self.i + movement_factor, self.j + 1) and\
                board[self.i + movement_factor][self.j + 1] != "noPiece" and\
                board[self.i + movement_factor][self.j + 1].get_color()\
                != self.color:
            move = "x%d,%d" % (self.i + movement_factor, self.j + 1)
            possible_moves.append(move)
        if self.is_bounded_square(self.i + movement_factor, self.j - 1) and\
                board[self.i + movement_factor][self.j - 1] == "noPiece" and\
                board[self.i][self.j - 1] != "noPiece" and\
                board[self.i][self.j - 1].color != self.color and\
                board[self.i][self.j - 1].rep == "P" and\
                board[self.i][self.j - 1].enpassant:
            move = "x%d,%d" % (self.i + movement_factor, self.j - 1)
            possible_moves.append(move)
        if self.is_bounded_square(self.i + movement_factor, self.j + 1) and\
                board[self.i + movement_factor][self.j + 1] == "noPiece" and\
                board[self.i][self.j + 1] != "noPiece" and\
                board[self.i][self.j + 1].color != self.color and\
                board[self.i][self.j + 1].rep == "P" and\
                board[self.i][self.j + 1].enpassant:
            move = "x%d,%d" % (self.i + movement_factor, self.j + 1)
            possible_moves.append(move)

        return possible_moves
