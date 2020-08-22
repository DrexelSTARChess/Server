from chessPiece import ChessPiece


class Knight(ChessPiece):
    """docstring for Knight"""

    def __init__(self, color, i, j):
        super(Knight, self).__init__(color, i, j)
        self.rep = "N"
        self.name = "Knight"

    def getPossibleMoves(self, board):
        possibleMoves = []
        movei = self.i + 2
        movej = self.j + 1
        if self.isBoundedSquare(movei, movej):
            if board[movei][movej] == "noPiece":
                move = "%d,%d" % (movei, movej)
                possibleMoves.append(move)
            elif board[movei][movej].color != self.color:
                move = "x%d,%d" % (movei, movej)
                possibleMoves.append(move)
        movei = self.i + 2
        movej = self.j - 1
        if self.isBoundedSquare(movei, movej):
            if board[movei][movej] == "noPiece":
                move = "%d,%d" % (movei, movej)
                possibleMoves.append(move)
            elif board[movei][movej].color != self.color:
                move = "x%d,%d" % (movei, movej)
                possibleMoves.append(move)
        movei = self.i - 2
        movej = self.j + 1
        if self.isBoundedSquare(movei, movej):
            if board[movei][movej] == "noPiece":
                move = "%d,%d" % (movei, movej)
                possibleMoves.append(move)
            elif board[movei][movej].color != self.color:
                move = "x%d,%d" % (movei, movej)
                possibleMoves.append(move)
        movei = self.i - 2
        movej = self.j - 1
        if self.isBoundedSquare(movei, movej):
            if board[movei][movej] == "noPiece":
                move = "%d,%d" % (movei, movej)
                possibleMoves.append(move)
            elif board[movei][movej].color != self.color:
                move = "x%d,%d" % (movei, movej)
                possibleMoves.append(move)
        # restart
        movei = self.i + 1
        movej = self.j + 2
        if self.isBoundedSquare(movei, movej):
            if board[movei][movej] == "noPiece":
                move = "%d,%d" % (movei, movej)
                possibleMoves.append(move)
            elif board[movei][movej].color != self.color:
                move = "x%d,%d" % (movei, movej)
                possibleMoves.append(move)
        movei = self.i + 1
        movej = self.j - 2
        if self.isBoundedSquare(movei, movej):
            if board[movei][movej] == "noPiece":
                move = "%d,%d" % (movei, movej)
                possibleMoves.append(move)
            elif board[movei][movej].color != self.color:
                move = "x%d,%d" % (movei, movej)
                possibleMoves.append(move)
        movei = self.i - 1
        movej = self.j + 2
        if self.isBoundedSquare(movei, movej):
            if board[movei][movej] == "noPiece":
                move = "%d,%d" % (movei, movej)
                possibleMoves.append(move)
            elif board[movei][movej].color != self.color:
                move = "x%d,%d" % (movei, movej)
                possibleMoves.append(move)
        movei = self.i - 1
        movej = self.j - 2
        if self.isBoundedSquare(movei, movej):
            if board[movei][movej] == "noPiece":
                move = "%d,%d" % (movei, movej)
                possibleMoves.append(move)
            elif board[movei][movej].color != self.color:
                move = "x%d,%d" % (movei, movej)
                possibleMoves.append(move)

        return possibleMoves
