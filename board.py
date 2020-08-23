from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn


class Board:
    """docstring for Board"""

    def __init__(self):
        super(Board, self).__init__()
        self.board = [
            [Rook("black", 0, 0), Knight("black", 0, 1), Bishop("black", 0, 2), Queen("black", 0, 3), King("black", 0, 4), Bishop("black", 0, 5), Knight("black", 0, 6), Rook("black", 0, 7)],
            [Pawn("black", 1, 0), Pawn("black", 1, 1), Pawn("black", 1, 2), Pawn("black", 1, 3), Pawn("black", 1, 4), Pawn("black", 1, 5), Pawn("black", 1, 6), Pawn("black", 1, 7)],
            ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
            ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
            ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
            ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
            [Pawn("white", 6, 0), Pawn("white", 6, 1), Pawn("white", 6, 2), Pawn("white", 6, 3), Pawn("white", 6, 4), Pawn("white", 6, 5), Pawn("white", 6, 6), Pawn("white", 6, 7)],
            [Rook("white", 7, 0), Knight("white", 7, 1),  Bishop("white", 7, 2), Queen("white", 7, 3), King("white", 7, 4), Bishop("white", 7, 5), Knight("white", 7, 6), Rook("white", 7, 7)]
        ]

    def setBoard(self, newBoard):
        """
        Take a Board object and set the board
        newBoard: the new value board will be set to
        """
        self.board = newBoard

    def getBoard(self):
        """
        A board getter
        Return: the Board object
        """
        return self.board

    def isSquareEmpty(self, x, y):
        """
        Checks if any piece is in a specified coordinate
        x: the x coordinate to be checked
        y: the y coordinate to be checked
        Return: boolean representing result
        """
        if self.board[x][y] == "noPiece":
            return True
        return False

    def isCheck(self, playerColor):
        """
        search for the king of the form:
        playerColor + King string, look in all directions for a piece
        if the piece is the same color, ignore
        else
            is the current king square being attacked? idk how to do this yet
        :param playerColor:
        :return:
        """

        ki = 0
        kj = 0
        for i in range(8):
            for j in range(8):
                if not self.isSquareEmpty(i, j) and self.board[i][j].rep == "K" and self.board[i][j].color == playerColor:  # find the king
                    ki = i
                    kj = j
        # print("found king at", ki, kj)
        allmoves = []
        for i in range(8):
            for j in range(8):
                if not self.isSquareEmpty(i, j) and self.board[i][j].color != playerColor:
                    allmoves += self.board[i][j].get_possible_moves(self.board)
        kings = "x%d,%d" % (ki, kj)
        if kings in allmoves:
            return True
        return False

    def quit(self, playerColor):
        return False

    def generateMoves(self, playerColor):
        """iterate through the board for all pieces begining in player color and calculate their moves"""

        for x in range(8):
            for y in range(8):
                if playerColor in self.board[x][y]:
                    return True  # replace this with move making method and append to list

        return []

    def isBoundedSquare(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

    def printBoardWhite(self):
        """testing, just print board"""
        print("-"*35)
        for i in range(8):
            for j in range(8):
                sq = self.board[i][j]
                if sq != "noPiece":
                    print(" " + self.board[i][j].get_piece_rep(), end=" ")
                else:
                    print(" //", end=" ")
            print()
            print()

    def printBoardBlack(self):
        print("-" * 35)
        for i in range(7, -1, -1):
            for j in range(7, -1, -1):
                sq = self.board[i][j]
                if sq != "noPiece":
                    print(" " + self.board[i][j].get_piece_rep(), end=" ")
                else:
                    print(" //", end=" ")
            print()
            print()

    def movePieceFast(self, x1, y1, x2, y2):
        # move piece internal location
        if self.board[x1][y1] != "noPiece":
            self.board[x1][y1].set_loc(x2, y2)
        if self.board[x2][y2] != "noPiece":
            self.board[x2][y2].set_loc(x1, y1)
        # move piece on board
        self.board[x1][y1], self.board[x2][y2] = self.board[x2][y2], self.board[x1][y1]

    def takePieceFast(self, x1, y1, x2, y2):
        # in this case, always assume the first piece is taking the place of the 2nd piece

        #change first piece location
        if self.board[x1][y1] != "noPiece":
            self.board[x1][y1].set_loc(x2, y2)

        #move piece on board
        self.board[x2][y2] = self.board[x1][y1]

        self.board[x1][y1] = "noPiece"

    def notKing(self, x, y):
        return self.board[x][y].rep != "K"

    def getLegalMoves(self, playerColor):
        """This function is to get all legal moves for pieces and format them nicely for Alex
            In addition, this is going to make sure that moves are legally applied as to not put the king in check
            If the amount of moves leaving this function is 0, then playerColor is in checkmate and the game is over

            In order to do this we must first iterate through every move of everypiece and add it to a new Board and then
            evaluate if there is a check for playerColor. If not, add to the legal movelist in a nice format, otherwise dont add it
            somewhere in here, take out attacking the king

            pray that this works somehow
            """
        legalMoves = []

        for i in range(8):
            for j in range(8):
                if not self.isSquareEmpty(i, j) and self.board[i][j].color == playerColor:  # for every piece...
                    # get the moveset of the piece...
                    piece = self.board[i][j]
                    moves = piece.get_possible_moves(self.board)
                    # and then the magic, apply each move here to a new board

                    # if piece.rep == "P":
                    #     print(moves)

                    for move in moves:
                        # first create a new board, and copy pieces
                        newBoard = Board()
                        for x in range(8):
                            for y in range(8):
                                if self.isSquareEmpty(x, y):
                                    newBoard.board[x][y] = "noPiece"
                                elif self.board[x][y].rep == "P":
                                    newBoard.board[x][y] = Pawn(self.board[x][y].color, x, y)
                                    newBoard.board[x][y].enpassant = self.board[x][y].enpassant
                                    newBoard.board[x][y].notMoved = self.board[x][y].notMoved
                                elif self.board[x][y].rep == "N":
                                    newBoard.board[x][y] = Knight(self.board[x][y].color, x, y)
                                elif self.board[x][y].rep == "B":
                                    newBoard.board[x][y] = Bishop(self.board[x][y].color, x, y)
                                elif self.board[x][y].rep == "Q":
                                    newBoard.board[x][y] = Queen(self.board[x][y].color, x, y)
                                elif self.board[x][y].rep == "R":
                                    newBoard.board[x][y] = Rook(self.board[x][y].color, x, y)
                                    newBoard.board[x][y].canCastle = self.board[x][y].canCastle
                                elif self.board[x][y].rep == "K":
                                    newBoard.board[x][y] = King(self.board[x][y].color, x, y)
                                    newBoard.board[x][y].canCastle = self.board[x][y].canCastle

                        # newBoard.printBoardWhite()
                        # print("MOVE: ", piece.color+piece.rep, move)
                        # print(newBoard.isCheck(playerColor))
                        # now apply the move of interest
                        if move.startswith("x"):
                            parseMove = move[1:].split(",")
                            takeX = int(parseMove[0])
                            takeY = int(parseMove[1])
                            newBoard.takePieceFast(i, j, takeX, takeY)
                        elif move.startswith("c"):
                            if "-" in move:
                                legalMoves.append([-1, 0, 0, 0])  # queen side castle
                            else:
                                legalMoves.append([0, 0, 0, -1])  # king side castle
                        else:
                            parseMove= move.split(",")
                            takeX = int(parseMove[0])
                            takeY = int(parseMove[1])
                            newBoard.takePieceFast(i, j, takeX, takeY)
                        # newBoard.printBoardWhite()
                        # now evaluate the board for check for playerColor
                        if not newBoard.isCheck(playerColor):
                            legalMoves.append([i, j, takeX, takeY])
                        # else:
                        #     print("ILLEGAL MOVE?:", piece.rep, "on", piece.getLoc(), move)

        return legalMoves

    def applyMove(self, playerColor, move):
        """Get move, apply move to board, Think about applying pawn promotion in this method"""
        for i in range(8):
            for j in range(8):
                if not self.isSquareEmpty(i, j) and self.board[i][j].rep == "P" and self.board[i][j].color == playerColor:  # turn off all your own enpassantable pieces now
                    self.board[i][j].enpassant = False

        # Apply move here according to rules
        """if pawn is moving 2 spaces set enpassant bool to True and change not moved to False
        check spefici en passant scenario if we are taking an en passant piece
        if king move set canCastle to False
        if rook move set canCastle to False
        if already castled sst canCastle to False
        """
        fx = move[0]
        fy = move[1]
        tx = move[2]
        ty = move[3]

        if move == [-1, 0, 0, 0] or move == [0, 0, 0, -1]:  # if we are castling
            if move == [0, 0, 0, -1]:  #king side castle
                if playerColor == "white":
                    self.board[7][4].canCastle = False
                    self.board[7][7].canCastle = False
                    self.board[7][0].canCastle = False
                    self.movePieceFast(7, 4, 7, 6)
                    self.movePieceFast(7, 7, 7, 5)

                else:
                    self.board[0][4].canCastle = False
                    self.board[0][7].canCastle = False
                    self.board[0][0].canCastle = False
                    self.movePieceFast(0, 4, 0, 6)
                    self.movePieceFast(0, 7, 0, 5)
            else:  # queen side castle
                if playerColor == "white":
                    self.board[7][4].canCastle = False
                    self.board[7][7].canCastle = False
                    self.board[7][0].canCastle = False
                    self.movePieceFast(7, 4, 7, 2)
                    self.movePieceFast(7, 0, 7, 3)
                else:
                    self.board[0][4].canCastle = False
                    self.board[0][7].canCastle = False
                    self.board[0][0].canCastle = False
                    self.movePieceFast(0, 4, 0, 2)
                    self.movePieceFast(0, 0, 0, 3)
        elif sum(move) >= 40:  # short hand for types of promotions
            for j in range(8):
                if not self.isSquareEmpty(0, j) and self.board[0][j].rep == "P":
                    if move == [10, 10, 10, 10]:
                        self.board[0][j] = Knight(playerColor, 0, j)
                    elif move == [20, 20, 20, 20]:
                        self.board[0][j] = Bishop(playerColor, 0, j)
                    elif move == [30, 30, 30, 30]:
                        self.board[0][j] = Rook(playerColor, 0, j)
                        self.board[0][j].canCastle = False
                    else:
                        self.board[0][j] = Queen(playerColor, 0, j)
                elif not self.isSquareEmpty(7, j) and self.board[7][j].rep == "P":
                    if move == [10, 10, 10, 10]:
                        self.board[7][j] = Knight(playerColor, 7, j)
                    elif move == [20, 20, 20, 20]:
                        self.board[7][j] = Bishop(playerColor, 7, j)
                    elif move == [30, 30, 30, 30]:
                        self.board[7][j] = Rook(playerColor, 7, j)
                        self.board[7][j].canCastle = False
                    else:
                        self.board[7][j] = Queen(playerColor, 7, j)
        else:

            pawnMovementFactor = 0
            if playerColor == "white":
                pawnMovementFactor = -1
            else:
                pawnMovementFactor = 1
            piece = self.board[fx][fy]
            if piece.rep == "K":
                piece.canCastle = False
            elif piece.rep == "R":
                piece.canCastle = False
            # first look at en passant i guess
            if piece.rep == "P" and abs(fx-tx) == 2 and self.isSquareEmpty(tx, ty):
                piece.enpassant = True  # make sure to check out pawn logic later
                piece.notMoved = False
                self.movePieceFast(fx, fy, tx, ty)
            elif piece.rep == "P" and self.isSquareEmpty(tx, ty) and self.isBoundedSquare(fx, fy-1) and not self.isSquareEmpty(fx, fy-1) and self.board[fx][fy-1].rep == "P" and self.board[fx][fy-1].enpassant:  # really come back and check this too
                # print("SHOULD FIRE")
                self.movePieceFast(fx, fy, tx, ty)
                self.board[fx][fy-1] = "noPiece"
            elif piece.rep == "P" and self.isSquareEmpty(tx, ty) and self.isBoundedSquare(fx, fy+1) and not self.isSquareEmpty(fx, fy+1) and self.board[fx][fy+1].rep == "P" and self.board[fx][fy+1].enpassant:  # really come back and check this too
                # print("SHOULD FIRE")
                self.movePieceFast(fx, fy, tx, ty)
                self.board[fx][fy+1] = "noPiece"
            elif piece.rep == "P" and abs(fx-tx) == 1 and self.isSquareEmpty(tx, ty):
                piece.notMoved = False
                self.movePieceFast(fx, fy, tx, ty)
            elif not self.isSquareEmpty(tx, ty):
                self.takePieceFast(fx, fy, tx, ty)
            else:
                self.movePieceFast(fx, fy, tx, ty)


        return True

    def generate_possible_moves(self, playerColor):
        # enemyColor = ""
        # if playerColor == "white":
        #     enemyColor = "black"
        # else:
        #     enemyColor = "white"
        #
        # enemyMoves = self.getLegalMoves(enemyColor) # used to return this

        return self.getLegalMoves(playerColor)

    def countPieces(self):
        total_pieces = 0
        for i in range(8):
            for j in range(8):
                if not self.isSquareEmpty(i, j):
                    total_pieces += 1
        return total_pieces

    def getWinner(self):
        """This function will return who won the game or if it was a draw"""
        if self.countPieces() == 2:
            return "draw"

        # for i in range(8):
        #     for j in range(8):
        #         if not self.isSquareEmpty(i, j):
        #             piece = self.board[i][j]
        #             if piece.rep == "K":
        #                 if piece.color == "white":
        #                     wKing = piece
        #                 else:
        #                     bKing = piece

        if len(self.getLegalMoves("white")) == 0:
            if self.isCheck("white"):
                return "black"
            else:
                return "draw"
        elif len(self.getLegalMoves("black")) == 0:
            if self.isCheck("black"):
                return "white"
            else:
                return "draw"
        else:
            return "draw"  # shouldn't really get here








