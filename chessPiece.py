from abc import ABC


class ChessPiece(ABC):
    """A chess piece is a fundamental building block of the chess board
    it contains knowledge of a real life chess piece which retains a consistent identity
    of color and movement type. This is basic to all chess pieces and will be coded as such.
    Movement instructions will be hardcoded as per the types of chess pieces
    """

    def __init__(self, color, i, j):
        self.color = color
        self.i = i
        self.j = j

    def getPossibleMoves(self, board):
        return [] # return a list of possible moves from a given board and location

    def getColor(self):
        return self.color

    def getPieceRep(self):
        if self.color == "white":
            return "w" + self.rep
        else:
            return "b" + self.rep

    def isBoundedSquare(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

    def setLoc(self, i, j):
        self.i = i
        self.j = j

    def getLoc(self):
        return "%d,%d" % (self.i, self.j)

    def getCardinals(self, board):
        possibleMoves = []

        tu = True  # true up, i, 0
        td = True  # true down -i, 0
        tl = True  # true left = j, 0
        tr = True  # true right = -j, 0
        ul = True  # up-left = i, j
        ur = True  # up-right = i, -j
        dl = True  # down-left = i, j
        dr = True  # down-left = i, -j

        for x in range(8):
            for y in range(8):
                if tu and self.isBoundedSquare(self.i + x, self.j) and x != 0:  # check up
                    newi = self.i + x
                    newj = self.j
                    if board[newi][newj] == "noPiece":  # empty square
                        move = "%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        pass
                    elif board[newi][newj].color != self.color:  # black piece thats not king
                        move = "x%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        tu = False
                        pass
                    else:  # white piece or black king, stop infront of it
                        tu = False
                        pass
                if td and self.isBoundedSquare(self.i - x, self.j) and x != 0:  # check down
                    newi = self.i - x
                    newj = self.j
                    if board[newi][newj] == "noPiece":  # empty square
                        move = "%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                            pass
                    elif board[newi][newj].color != self.color:  # black piece thats not king
                        move = "x%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        td = False
                        pass
                    else:  # white piece or black king, stop infront of it
                        td = False
                        pass
                if tl and self.isBoundedSquare(self.i, self.j + y) and y != 0:  # check left
                    newi = self.i
                    newj = self.j + y
                    if board[newi][newj] == "noPiece":  # empty square
                        move = "%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                    elif board[newi][newj].color != self.color:  # black piece thats not king
                        move = "x%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        tl = False
                        pass
                    else:  # white piece or black king, stop infront of it
                        tl = False
                        pass
                if tr and self.isBoundedSquare(self.i, self.j - y) and y != 0:  # check right
                    newi = self.i
                    newj = self.j - y
                    if board[newi][newj] == "noPiece":  # empty square
                        move = "%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                    elif board[newi][newj].color != self.color:  # black piece thats not king
                        move = "x%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        tl = False
                        pass
                    else:  # white piece or black king, stop infront of it
                        tl = False
                        pass

        return possibleMoves

    def getDiagnals(self, board):
        possibleMoves = []

        tu = True  # true up, i, 0
        td = True  # true down -i, 0
        tl = True  # true left = j, 0
        tr = True  # true right = -j, 0
        ul = True  # up-left = i, j
        ur = True  # up-right = i, -j
        dl = True  # down-left = i, j
        dr = True  # down-left = i, -j

        for x in range(8):
            for y in range(8):
                if ul and self.isBoundedSquare(self.i + x, self.j + x) and x != 0:  # check up left
                    newi = self.i + x
                    newj = self.j + x
                    if board[newi][newj] == "noPiece":  # empty square
                        move = "%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                    elif board[newi][newj].color != self.color:  # black piece thats not king
                        move = "x%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        ul = False
                        pass
                    else:  # white piece or black king, stop infront of it
                        ul = False
                        pass
                if ur and self.isBoundedSquare(self.i + x, self.j - x) and x != 0:  # check up right
                    newi = self.i + x
                    newj = self.j - x
                    if board[newi][newj] == "noPiece":  # empty square
                        move = "%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                    elif board[newi][newj].color != self.color:  # black piece thats not king
                        move = "x%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        ur = False
                        pass
                    else:  # white piece or black king, stop infront of it
                        ur = False
                        pass
                if dl and self.isBoundedSquare(self.i - x, self.j + x) and x != 0:  # check down left
                    newi = self.i - x
                    newj = self.j + x
                    if board[newi][newj] == "noPiece":  # empty square
                        move = "%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                    elif board[newi][newj].color != self.color:  # black piece thats not king
                        move = "x%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        dl = False
                        pass
                    else:  # white piece or black king, stop infront of it
                        dl = False
                        pass
                if dr and self.isBoundedSquare(self.i - x, self.j - x) and x != 0:  # check down right
                    newi = self.i - x
                    newj = self.j - x
                    if board[newi][newj] == "noPiece":  # empty square
                        move = "%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                    elif board[newi][newj].color != self.color:  # black piece thats not king
                        move = "x%d,%d" % (newi, newj)
                        if move not in possibleMoves:
                            possibleMoves.append(move)
                        dr = False
                        pass
                    else:  # white piece or black king, stop infront of it
                        dr = False
                        pass

        return possibleMoves

    def getKnight(self, board):
        possibleMoves = []
        movei = self.i + 2
        movej = self.j + 1
        if self.isBoundedSquare(movei, movej) and ((board[movei][movej] == "noPiece") or (
                board[movei][movej].color != self.color)):
            move = "%d,%d" % (movei, movej)
            possibleMoves.append(move)
        movei = self.i + 2
        movej = self.j - 1
        if self.isBoundedSquare(movei, movej) and ((board[movei][movej] == "noPiece") or (
                        board[movei][movej].color != self.color)):
            move = "%d,%d" % (movei, movej)
            possibleMoves.append(move)
        movei = self.i - 2
        movej = self.j + 1
        if self.isBoundedSquare(movei, movej) and ((board[movei][movej] == "noPiece") or (
                        board[movei][movej].color != self.color)):
            move = "%d,%d" % (movei, movej)
            possibleMoves.append(move)
        movei = self.i - 2
        movej = self.j - 1
        if self.isBoundedSquare(movei, movej) and ((board[movei][movej] == "noPiece") or (
                        board[movei][movej].color != self.color)):
            move = "%d,%d" % (movei, movej)
            possibleMoves.append(move)
        ### restart
        movei = self.i + 1
        movej = self.j + 2
        if self.isBoundedSquare(movei, movej) and ((board[movei][movej] == "noPiece") or (
                        board[movei][movej].color != self.color)):
            move = "%d,%d" % (movei, movej)
            possibleMoves.append(move)
        movei = self.i + 1
        movej = self.j - 2
        if self.isBoundedSquare(movei, movej) and ((board[movei][movej] == "noPiece") or (
                        board[movei][movej].color != self.color)):
            move = "%d,%d" % (movei, movej)
            possibleMoves.append(move)
        movei = self.i - 1
        movej = self.j + 2
        if self.isBoundedSquare(movei, movej) and ((board[movei][movej] == "noPiece") or (
                        board[movei][movej].color != self.color)):
            move = "%d,%d" % (movei, movej)
            possibleMoves.append(move)
        movei = self.i - 1
        movej = self.j - 2
        if self.isBoundedSquare(movei, movej) and ((board[movei][movej] == "noPiece") or (
                        board[movei][movej].color != self.color)):
            move = "%d,%d" % (movei, movej)
            possibleMoves.append(move)

        return possibleMoves
