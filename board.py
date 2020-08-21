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
            [Rook("white", 0, 0), Knight("white", 0, 1), Bishop("white", 0, 2), King("white", 0, 3), Queen("white", 0, 4), Bishop("white", 0, 5), Knight("white", 0, 6), Rook("white", 0, 7)],
            [Pawn("white", 1, 0), Pawn("white", 1, 1), Pawn("white", 1, 2), Pawn("white", 1, 3), Pawn("white", 1, 4), Pawn("white", 1, 5), Pawn("white", 1, 6), Pawn("white", 1, 7)],
            ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
            ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
            ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
            ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
            [Pawn("black", 6, 0), Pawn("black", 6, 1), Pawn("black", 6, 2), Pawn("black", 6, 3), Pawn("black", 6, 4), Pawn("black", 6, 5), Pawn("black", 6, 6), Pawn("black", 6, 7)],
            [Rook("black", 7, 0), Knight("black", 7, 1),  Bishop("black", 7, 2), King("black", 7, 3), Queen("black", 7, 4), Bishop("black", 7, 5), Knight("black", 7, 6), Rook("black", 7, 7)]
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
                if not self.isSquareEmpty(i, j) and self.board[i][j].rep == "K":  # find the king
                    ki = i
                    kj = j
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

    def printBoardBlack(self):
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

    def printBoardWhite(self):
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





