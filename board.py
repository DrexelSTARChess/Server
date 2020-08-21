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

    def isGameOver(self):
        """
        Check if checkmate was achieved, i think we should provide a color here but i guess we dont have to
        we need to iterate first in the board and look for the king, then see if in check, then check surrounding squares
        :return: boolean representing if the game is over
        """
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
                    allmoves += self.board[i][j].getPossibleMoves(self.board)
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

    def printBoardWhite(self):
        """testing, just print board"""
        print("-"*35)
        for i in range(8):
            for j in range(8):
                sq = self.board[i][j]
                if sq != "noPiece":
                    print(" " + self.board[i][j].getPieceRep(), end=" ")
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
                    print(" " + self.board[i][j].getPieceRep(), end=" ")
                else:
                    print(" //", end=" ")
            print()
            print()

    def movePieceFast(self, x1, y1, x2, y2):
        # move piece internal location
        if self.board[x1][y1] != "noPiece":
            self.board[x1][y1].setLoc(x2, y2)
        if self.board[x2][y2] != "noPiece":
            self.board[x2][y2].setLoc(x1, y1)
        # move piece on board
        self.board[x1][y1], self.board[x2][y2] = self.board[x2][y2], self.board[x1][y1]

    def takePieceFast(self, x1, y1, x2, y2):
        # in this case, always assume the first piece is taking the place of the 2nd piece

        #change first piece location
        if self.board[x1][y1] != "noPiece":
            self.board[x1][y1].setLoc(x2, y2)

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
                    moves = piece.getPossibleMoves(self.board)
                    # and then the magic, apply each move here to a new board

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
                                legalMoves.append([0, 0, 0, 0])  # queen side castle
                            else:
                                legalMoves.append([1, 0, 0, 0])  # king side castle
                        else:
                            parseMove= move.split(",")
                            takeX = int(parseMove[0])
                            takeY = int(parseMove[1])
                            newBoard.takePieceFast(i, j, takeX, takeY)
                        # newBoard.printBoardWhite()
                        # now evaluate the board for check for playerColor
                        if not newBoard.isCheck(playerColor):
                            legalMoves.append([i, j, takeX, takeY])

        return legalMoves





