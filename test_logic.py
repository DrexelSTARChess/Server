from unittest import TestCase
from board import Board


class TestLogic(TestCase):
    def test_pawn(self):
        b = Board()
        pawn_moves = b.board[6][4].get_possible_moves(b.board)
        assert pawn_moves == ['4,4', '5,4']  # double move on first move
        b.move_piece_fast(6, 4, 4, 4)
        b.board[4][4].not_moved = False
        b.move_piece_fast(1, 3, 3, 3)
        b.board[3][3].not_moved = False
        pawn_moves = b.board[4][4].get_possible_moves(b.board)
        assert pawn_moves == ['3,4', 'x3,3']  # moving or taking
        b.move_piece_fast(4, 4, 3, 4)
        b.board[3][3].enpassant = True
        pawn_moves = b.board[3][4].get_possible_moves(b.board)
        assert pawn_moves == ['2,4', 'x2,3']  # en passant or pass

    def test_knight(self):
        b = Board()
        b.move_piece_fast(7, 1, 5, 2)
        # knight moves
        knight_moves = b.board[5][2].get_possible_moves(b.board)
        assert knight_moves == ['7,1', '3,3', '3,1', '4,4', '4,0']

    def testBishop(self):
        b = Board()
        b.move_piece_fast(7, 2, 4, 3)
        bishop_moves = b.board[4][3].get_possible_moves(b.board)
        # bishop moves
        assert bishop_moves ==\
               ['5,4', '5,2', '3,4', '3,2', '2,5', '2,1', 'x1,6', 'x1,0']

    def test_rook(self):
        b = Board()
        b.move_piece_fast(7, 0, 4, 3)
        rook_moves = b.board[4][3].get_possible_moves(b.board)
        # rook moves
        assert rook_moves == [
            '4,4',
            '4,2',
            '4,5',
            '4,1',
            '4,6',
            '4,0',
            '4,7',
            '5,3',
            '3,3',
            '2,3',
            'x1,3'
        ]

    def test_queen(self):
        b = Board()
        b.move_piece_fast(7, 3, 4, 3)
        queen_moves = b.board[4][3].get_possible_moves(b.board)
        # queen moves
        assert queen_moves == [
            '4,4',
            '4,2',
            '4,5',
            '4,1',
            '4,6',
            '4,0',
            '4,7',
            '5,3',
            '3,3',
            '2,3',
            'x1,3',
            '5,4',
            '5,2',
            '3,4',
            '3,2',
            '2,5',
            '2,1',
            'x1,6',
            'x1,0'
        ]

    def test_king(self):
        b = Board()
        b.move_piece_fast(7, 4, 4, 3)
        king_moves = b.board[4][3].get_possible_moves(b.board)
        # king moves
        assert king_moves ==\
               ['5,3', '3,3', '4,4', '4,2', '5,4', '5,2', '3,4', '3,2']

    def test_is_check(self):
        b = Board()
        assert not b.is_check("black")  # not in check
        b.move_piece_fast(1, 4, 3, 7)
        b.move_piece_fast(7, 3, 5, 4)
        assert b.is_check("black")  # is in check

    def test_first_moves(self):
        b = Board()
        # all first moves are consistent
        first_moves = b.get_legal_moves("white")
        assert first_moves == [
            [6, 0, 4, 0],
            [6, 0, 5, 0],
            [6, 1, 4, 1],
            [6, 1, 5, 1],
            [6, 2, 4, 2],
            [6, 2, 5, 2],
            [6, 3, 4, 3],
            [6, 3, 5, 3],
            [6, 4, 4, 4],
            [6, 4, 5, 4],
            [6, 5, 4, 5],
            [6, 5, 5, 5],
            [6, 6, 4, 6],
            [6, 6, 5, 6],
            [6, 7, 4, 7],
            [6, 7, 5, 7],
            [7, 1, 5, 2],
            [7, 1, 5, 0],
            [7, 6, 5, 7],
            [7, 6, 5, 5]
        ]
        b.apply_move("white", [6, 0, 4, 0])
        second_moves = b.get_legal_moves("white")
        assert second_moves == [
            [4, 0, 3, 0],
            [6, 1, 4, 1],
            [6, 1, 5, 1],
            [6, 2, 4, 2],
            [6, 2, 5, 2],
            [6, 3, 4, 3],
            [6, 3, 5, 3],
            [6, 4, 4, 4],
            [6, 4, 5, 4],
            [6, 5, 4, 5],
            [6, 5, 5, 5],
            [6, 6, 4, 6],
            [6, 6, 5, 6],
            [6, 7, 4, 7],
            [6, 7, 5, 7],
            [7, 0, 6, 0],
            [7, 0, 5, 0],
            [7, 1, 5, 2],
            [7, 1, 5, 0],
            [7, 6, 5, 7],
            [7, 6, 5, 5]
        ]

    def test_fools_mate(self):
        b = Board()
        b.move_piece_fast(6, 5, 5, 5)
        b.move_piece_fast(1, 4, 3, 4)
        b.move_piece_fast(6, 6, 4, 6)
        b.move_piece_fast(0, 3, 4, 7)
        assert b.get_winner() == "black"

    def test_scholars_mate(self):
        b = Board()
        b.move_piece_fast(6, 4, 4, 4)
        b.move_piece_fast(1, 4, 3, 4)
        b.move_piece_fast(7, 5, 4, 2)
        b.move_piece_fast(0, 1, 2, 2)
        b.move_piece_fast(7, 3, 3, 7)
        b.move_piece_fast(0, 6, 2, 5)
        b.take_piece_fast(3, 7, 1, 5)
        assert b.get_winner() == "white"

    def test_castle_king(self):
        b = Board()
        b.move_piece_fast(7, 5, 5, 5)
        b.move_piece_fast(7, 6, 5, 6)
        b.move_piece_fast(7, 3, 5, 3)
        b.move_piece_fast(7, 2, 5, 2)
        b.move_piece_fast(7, 1, 5, 1)
        # BUG FOUND HERE, SOLVED
        print(b.board[7][4].get_possible_moves(b.board))
        b.apply_move("white", [0, 0, 0, -1])
        assert b.board[7][6].rep == "K" and\
               b.board[7][5].rep == "R" and\
               b.board[7][7] == "noPiece"
        b.print_board_white()

    def test_castle_queen(self):
        b = Board()
        b.move_piece_fast(7, 5, 5, 5)
        b.move_piece_fast(7, 6, 5, 6)
        b.move_piece_fast(7, 3, 5, 3)
        b.move_piece_fast(7, 2, 5, 2)
        b.move_piece_fast(7, 1, 5, 1)
        # BUG FOUND HERE, SOLVED
        print(b.board[7][4].get_possible_moves(b.board))
        b.apply_move("white", [-1, 0, 0, 0])
        assert b.board[7][2].rep == "K" and\
               b.board[7][3].rep == "R" and\
               b.board[7][1] == "noPiece"
        b.print_board_white()
