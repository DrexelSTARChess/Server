from board import Board

if __name__ == "__main__":
    b = Board()

    """we gott put this into a pawn test case, idk how"""
    # print(b.board[1][0].getPossibleMoves(b.board))
    #
    # b.movePieceFast(1, 1, 4, 5)
    # b.movePieceFast(6, 1, 2, 1)
    #
    # b.printBoardWhite()
    # print(b.board[2][1].getPossibleMoves(b.board))
    # b.takePieceFast(2, 1, 1, 0)
    # b.printBoardWhite()
    # print(b.board[1][0].getPossibleMoves(b.board))

    """Queen test case p1"""
    # b.movePieceFast(0, 4, 3, 4)
    # print(b.board[3][4].getLoc())
    # print(b.board[3][4].getPossibleMoves(b.board))
    # b.printBoardWhite()

    """Queen test case p2"""
    # b.movePieceFast(0, 4, 3, 3)
    # b.movePieceFast(6, 3, 2, 6)
    # print(b.board[3][3].getLoc())
    # print(b.board[3][3].getPossibleMoves(b.board))
    # print("Is the king in check?", b.isCheck("black"))
    # b.printBoardWhite()

    """Rook test case"""
    # b.movePieceFast(0, 0, 4, 2)
    # print(b.board[4][2].getPossibleMoves(b.board))
    # b.printBoardWhite()

    """Bishop test case"""
    # b.movePieceFast(0, 2, 4, 2)
    # print(b.board[4][2].getPossibleMoves(b.board))
    # b.printBoardWhite()


    """Knight test"""
    # b.movePieceFast(0, 1, 5, 2)
    # print(b.board[5][2].getLoc())
    # print(b.board[5][2].getPossibleMoves(b.board))
    # print("Is the king in check?", b.isCheck("black"))
    # b.printBoardWhite()

    """King test"""
    # b.movePieceFast(0, 3, 5, 2)
    # print(b.board[5][2].getLoc())
    # print(b.board[5][2].getPossibleMoves(b.board))
    # print("Is the king in check?", b.isCheck("white"))
    # b.printBoardWhite()

    # for i in range(8):
    #     for j in range(8):
    #         piece = b.board[i][j]
    #         if piece != "noPiece" and piece.color == "white":
    #             moves = piece.getPossibleMoves(b.board)
    #             if len(moves) == 0:
    #                 print(piece.rep, "at ", i, j, "has no moves")
    #             else:
    #                 print(piece.rep, "at ", i, j, "has: ", moves)


    """Fool's mate test (white mated)"""
    # b.movePieceFast(6, 5, 5, 5)
    # b.movePieceFast(1, 4, 3, 4)
    # b.movePieceFast(6, 6, 4, 6)
    # b.movePieceFast(0, 3, 4, 7)

    """Scholar's Mate (black mated)"""
    # b.movePieceFast(6, 4, 4, 4)
    # b.movePieceFast(1, 4, 3, 4)
    # b.movePieceFast(7, 5, 4, 2)
    # b.movePieceFast(0, 1, 2, 2)
    # b.movePieceFast(7, 3, 3, 7)
    # b.movePieceFast(0, 6, 2, 5)
    # b.takePieceFast(3, 7, 1, 5)

    # b.printBoardWhite()

    # b.movePieceFast(0, 0, 5, 4)

    """Castle tests"""
    # b.movePieceFast(0, 5, 5, 5)
    # b.movePieceFast(0, 6, 5, 6)
    # b.movePieceFast(0, 3, 5, 3)
    # b.movePieceFast(0, 2, 5, 2)
    # b.movePieceFast(0, 1, 5, 1)

    """En Passant test"""
    # b.movePieceFast(1, 5, 4, 5)
    # b.movePieceFast(6, 6, 4, 6)



    # print("Is the king in check?", b.isCheck("white"))
    b.printBoardWhite()

    print(b.getLegalMoves("white"))


