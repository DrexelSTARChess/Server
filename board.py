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
            [
                Rook("black", 0, 0),
                Knight("black", 0, 1),
                Bishop("black", 0, 2),
                Queen("black", 0, 3),
                King("black", 0, 4),
                Bishop("black", 0, 5),
                Knight("black", 0, 6),
                Rook("black", 0, 7)
            ],
            [
                Pawn("black", 1, 0),
                Pawn("black", 1, 1),
                Pawn("black", 1, 2),
                Pawn("black", 1, 3),
                Pawn("black", 1, 4),
                Pawn("black", 1, 5),
                Pawn("black", 1, 6),
                Pawn("black", 1, 7)
            ],
            [
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece"
            ],
            [
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece"
            ],
            [
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece"
            ],
            [
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece",
                "noPiece"
            ],
            [
                Pawn("white", 6, 0),
                Pawn("white", 6, 1),
                Pawn("white", 6, 2),
                Pawn("white", 6, 3),
                Pawn("white", 6, 4),
                Pawn("white", 6, 5),
                Pawn("white", 6, 6),
                Pawn("white", 6, 7)
            ],
            [
                Rook("white", 7, 0),
                Knight("white", 7, 1),
                Bishop("white", 7, 2),
                Queen("white", 7, 3),
                King("white", 7, 4),
                Bishop("white", 7, 5),
                Knight("white", 7, 6),
                Rook("white", 7, 7)
            ]
        ]

    def set_board(self, new_board):
        """
        Take a Board object and set the board
        newBoard: the new value board will be set to
        """
        self.board = new_board

    def get_board(self):
        """
        A board getter
        Return: the Board object
        """
        return self.board

    def is_square_empty(self, x, y):
        """
        Checks if any piece is in a specified coordinate
        x: the x coordinate to be checked
        y: the y coordinate to be checked
        Return: boolean representing result
        """
        if self.board[x][y] == "noPiece":
            return True
        return False

    def is_check(self, player_color):
        """
        search for the king of the form:
        playerColor + King string, look in all directions for a piece
        if the piece is the same color, ignore
        else
            is the current king square being attacked? idk how to do this yet
        :param player_color:
        :return:
        """

        ki = 0
        kj = 0
        for i in range(8):
            for j in range(8):
                # find the king
                if not self.is_square_empty(i, j) and\
                        self.board[i][j].rep == "K" and\
                        self.board[i][j].color == player_color:
                    ki = i
                    kj = j
        # print("found king at", ki, kj)
        allmoves = []
        for i in range(8):
            for j in range(8):
                if not self.is_square_empty(i, j) and\
                        self.board[i][j].color != player_color:
                    allmoves +=\
                        self.board[i][j].get_possible_moves(self.board)
        kings = "x%d,%d" % (ki, kj)
        if kings in allmoves:
            return True
        return False

    def quit(self, playerColor):
        return False

    def generate_moves(self, playerColor):
        """
        iterate through the board for all pieces beginning
        in player color and calculate their moves
        """

        for x in range(8):
            for y in range(8):
                # replace this with move making method and append to list
                if playerColor in self.board[x][y]:
                    return True

        return []

    def is_bounded_square(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

    def print_board_white(self):
        """testing, just print board"""
        print("-" * 35)
        for i in range(8):
            for j in range(8):
                sq = self.board[i][j]
                if sq != "noPiece":
                    print(" " + self.board[i][j].get_piece_rep(), end=" ")
                else:
                    print(" //", end=" ")
            print()
            print()

    def print_board_black(self):
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

    def move_piece_fast(self, x1, y1, x2, y2):
        # move piece internal location
        if self.board[x1][y1] != "noPiece":
            self.board[x1][y1].set_loc(x2, y2)
        if self.board[x2][y2] != "noPiece":
            self.board[x2][y2].set_loc(x1, y1)
        # move piece on board
        self.board[x1][y1], self.board[x2][y2] =\
            self.board[x2][y2], self.board[x1][y1]

    def take_piece_fast(self, x1, y1, x2, y2):
        # in this case, always assume the first piece
        # is taking the place of the 2nd piece

        # change first piece location
        if self.board[x1][y1] != "noPiece":
            self.board[x1][y1].set_loc(x2, y2)

        # move piece on board
        self.board[x2][y2] = self.board[x1][y1]

        self.board[x1][y1] = "noPiece"

    def not_king(self, x, y):
        return self.board[x][y].rep != "K"

    def get_legal_moves(self, player_color):
        """
        This function is to get all legal moves for pieces
        and format them nicely for Alex
        In addition, this is going to make sure that moves
        are legally applied as to not put the king in check
        If the amount of moves leaving this function is 0,
        then playerColor is in checkmate and the game is over

        In order to do this we must first iterate through
        every move of everypiece and add it to a new Board and then
        evaluate if there is a check for playerColor.
        If not, add to the legal movelist in a nice format,
        otherwise dont add it somewhere in here, take out attacking the king

        pray that this works somehow
        """
        legal_moves = []

        for i in range(8):
            for j in range(8):
                # for every piece...
                if not self.is_square_empty(i, j) and\
                        self.board[i][j].color == player_color:
                    # get the moveset of the piece...
                    piece = self.board[i][j]
                    moves = piece.get_possible_moves(self.board)
                    # and then the magic, apply each move here to a new board

                    for move in moves:
                        # first create a new board, and copy pieces
                        new_board = Board()
                        for x in range(8):
                            for y in range(8):
                                if self.is_square_empty(x, y):
                                    new_board.board[x][y] = "noPiece"
                                elif self.board[x][y].rep == "P":
                                    new_board.board[x][y] =\
                                        Pawn(self.board[x][y].color, x, y)
                                    new_board.board[x][y].enpassant =\
                                        self.board[x][y].enpassant
                                    new_board.board[x][y].not_moved =\
                                        self.board[x][y].not_moved
                                elif self.board[x][y].rep == "N":
                                    new_board.board[x][y] =\
                                        Knight(self.board[x][y].color, x, y)
                                elif self.board[x][y].rep == "B":
                                    new_board.board[x][y] =\
                                        Bishop(self.board[x][y].color, x, y)
                                elif self.board[x][y].rep == "Q":
                                    new_board.board[x][y] =\
                                        Queen(self.board[x][y].color, x, y)
                                elif self.board[x][y].rep == "R":
                                    new_board.board[x][y] =\
                                        Rook(self.board[x][y].color, x, y)
                                    new_board.board[x][y].can_castle =\
                                        self.board[x][y].can_castle
                                elif self.board[x][y].rep == "K":
                                    new_board.board[x][y] =\
                                        King(self.board[x][y].color, x, y)
                                    new_board.board[x][y].can_castle =\
                                        self.board[x][y].can_castle

                        # now apply the move of interest
                        if move.startswith("x"):
                            parse_move = move[1:].split(",")
                            take_x = int(parse_move[0])
                            take_y = int(parse_move[1])
                            new_board.take_piece_fast(i, j, take_x, take_y)
                        elif move.startswith("c"):
                            if player_color == "white":
                                if "-" in move:
                                    # queen side castle
                                    # check every location of the king in castle move
                                    new_board.move_piece_fast(7, 4, 7, 3)
                                    if new_board.is_check(player_color):
                                        continue
                                    new_board.move_piece_fast(7, 3, 7, 2)
                                    if new_board.is_check(player_color):
                                        continue
                                    #  made it this far, append a white queenside castle
                                    legal_moves.append([7, 4, 7, 2])
                                else:  # kingside castle
                                    new_board.move_piece_fast(7, 4, 7, 5)
                                    if new_board.is_check(player_color):
                                        continue
                                    new_board.move_piece_fast(7, 5, 7, 6)
                                    if new_board.is_check(player_color):
                                        continue
                                    legal_moves.append([7, 4, 7, 6])

                            else:  # is black
                                if "-" in move:
                                    # queen side castle
                                    # check every location of the king in castle move
                                    new_board.move_piece_fast(0, 4, 0, 3)
                                    if new_board.is_check(player_color):
                                        continue
                                    new_board.move_piece_fast(0, 3, 0, 2)
                                    if new_board.is_check(player_color):
                                        continue
                                    #  made it this far, append a black queenside castle
                                    legal_moves.append([0, 4, 0, 2])
                                else:  # kingside castle
                                    new_board.move_piece_fast(0, 4, 0, 5)
                                    if new_board.is_check(player_color):
                                        continue
                                    new_board.move_piece_fast(0, 5, 0, 6)
                                    if new_board.is_check(player_color):
                                        continue
                                    legal_moves.append([0, 4, 0, 6])
                        else:
                            parse_move = move.split(",")
                            take_x = int(parse_move[0])
                            take_y = int(parse_move[1])
                            new_board.take_piece_fast(i, j, take_x, take_y)
                        # now evaluate the board for check for playerColor
                        if not new_board.is_check(player_color):
                            legal_moves.append([i, j, take_x, take_y])

        return legal_moves

    def apply_move(self, player_color, move):
        """
        Get move, apply move to board,
        Think about applying pawn promotion in this method
        """
        for i in range(8):
            for j in range(8):
                # turn off all your own enpassantable pieces now
                if not self.is_square_empty(i, j) and\
                        self.board[i][j].rep == "P" and\
                        self.board[i][j].color == player_color:
                    self.board[i][j].enpassant = False

        # Apply move here according to rules
        """
        if pawn is moving 2 spaces set enpassant bool to True
        and change not moved to False
        check specific en passant scenario if taking an en passant piece
        if king move set canCastle to False
        if rook move set canCastle to False
        if already castled sst canCastle to False
        """
        fx = move[0]
        fy = move[1]
        tx = move[2]
        ty = move[3]

        # if we are castling
        if move == [7, 4, 7, 6]:  # white kingside castle
                self.board[7][4].can_castle = False
                self.board[7][7].can_castle = False
                self.board[7][0].can_castle = False
                self.move_piece_fast(7, 4, 7, 6)
                self.move_piece_fast(7, 7, 7, 5)

        elif move == [0, 4, 0, 6]:  # black kingside castle
                self.board[0][4].can_castle = False
                self.board[0][7].can_castle = False
                self.board[0][0].can_castle = False
                self.move_piece_fast(0, 4, 0, 6)
                self.move_piece_fast(0, 7, 0, 5)
        elif move == [7, 4, 7, 2]:  # white queenside castle
                self.board[7][4].can_castle = False
                self.board[7][7].can_castle = False
                self.board[7][0].can_castle = False
                self.move_piece_fast(7, 4, 7, 2)
                self.move_piece_fast(7, 0, 7, 3)
        elif move == [0, 4, 0, 2]:  # black queenside castle
                    self.board[0][4].can_castle = False
                    self.board[0][7].can_castle = False
                    self.board[0][0].can_castle = False
                    self.move_piece_fast(0, 4, 0, 2)
                    self.move_piece_fast(0, 0, 0, 3)
        elif sum(move) >= 40:  # short hand for types of promotions
            if not self.is_square_empty(1, move[1]) and\
                    self.board[1][move[1]].rep == "P" and \
                    self.board[1][move[1]].color == "white":
                if move[2:] == [20, 20]:
                    self.board[0][move[1]] = Knight(player_color, 0, move[1])
                    self.board[1][move[1]] = "noPiece"
                elif move[2:] == [30, 30]:
                    self.board[0][move[1]] = Bishop(player_color, 0, move[1])
                    self.board[1][move[1]] = "noPiece"
                elif move[2:] == [40, 40]:
                    self.board[0][move[1]] = Rook(player_color, 0, move[1])
                    self.board[0][move[1]].can_castle = False
                    self.board[1][move[1]] = "noPiece"
                else:
                    self.board[0][move[1]] = Queen(player_color, 0, move[1])
                    self.board[1][move[1]] = "noPiece"
            elif not self.is_square_empty(6, move[1]) and\
                    self.board[7][move[1]].rep == "P" and \
                    self.board[1][move[1]].color == "black":
                if move[2:] == [20, 20]:
                    self.board[7][move[1]] = Knight(player_color, 7, move[1])
                    self.board[6][move[1]] = "noPiece"
                elif move[2:] == [30, 30]:
                    self.board[7][move[1]] = Bishop(player_color, 7, move[1])
                    self.board[6][move[1]] = "noPiece"
                elif move[2:] == [40, 40]:
                    self.board[7][move[1]] = Rook(player_color, 7, move[1])
                    self.board[7][move[1]].can_castle = False
                    self.board[6][move[1]] = "noPiece"
                else:
                    self.board[7][move[1]] = Queen(player_color, 7, move[1])
                    self.board[6][move[1]] = "noPiece"
        else:
            piece = self.board[fx][fy]
            if piece.rep == "K":
                piece.can_castle = False
            elif piece.rep == "R":
                piece.can_castle = False
            # first look at en passant i guess
            if piece.rep == "P" and\
                    abs(fx - tx) == 2 and\
                    self.is_square_empty(tx, ty):
                # make sure to check out pawn logic later
                piece.enpassant = True
                piece.not_moved = False
                self.move_piece_fast(fx, fy, tx, ty)
            # really come back and check this too
            elif piece.rep == "P" and\
                    self.is_square_empty(tx, ty) and\
                    self.is_bounded_square(fx, fy - 1) and\
                    not self.is_square_empty(fx, fy - 1) and\
                    self.board[fx][fy - 1].rep == "P" and\
                    self.board[fx][fy - 1].enpassant:
                self.move_piece_fast(fx, fy, tx, ty)
                self.board[fx][fy - 1] = "noPiece"
            # really come back and check this too
            elif piece.rep == "P" and\
                    self.is_square_empty(tx, ty) and\
                    self.is_bounded_square(fx, fy + 1) and\
                    not self.is_square_empty(fx, fy + 1) and\
                    self.board[fx][fy + 1].rep == "P" and\
                    self.board[fx][fy + 1].enpassant:
                self.move_piece_fast(fx, fy, tx, ty)
                self.board[fx][fy + 1] = "noPiece"
            elif piece.rep == "P" and\
                    abs(fx - tx) == 1 and\
                    self.is_square_empty(tx, ty):
                piece.not_moved = False
                self.move_piece_fast(fx, fy, tx, ty)
            elif not self.is_square_empty(tx, ty):
                self.take_piece_fast(fx, fy, tx, ty)
            else:
                self.move_piece_fast(fx, fy, tx, ty)

        return True

    def generate_possible_moves(self, player_color):
        return self.get_legal_moves(player_color)

    def count_pieces(self):
        total_pieces = 0
        for i in range(8):
            for j in range(8):
                if not self.is_square_empty(i, j):
                    total_pieces += 1
        return total_pieces

    def get_winner(self):
        """This function will return who won the game or if it was a draw"""
        if self.count_pieces() == 2:
            return "draw"

        if len(self.get_legal_moves("white")) == 0:
            if self.is_check("white"):
                return "black"
            else:
                return "draw"
        elif len(self.get_legal_moves("black")) == 0:
            if self.is_check("black"):
                return "white"
            else:
                return "draw"
        else:
            return "draw"  # shouldn't really get here
