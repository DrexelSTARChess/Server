from board import Board
import random
import time

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

    """Queen test case p2 <<< This one is good"""
    # b.movePieceFast(1, 4, 3, 7)
    # b.movePieceFast(7, 3, 5, 4)
    # print("Is the king in check?", b.isCheck("black"))
    # b.printBoardWhite()

    """Rook test case"""
    # b.movePieceFast(7, 7, 4, 5)
    # b.movePieceFast(6, 3, 2, 2)
    # b.movePieceFast(6, 4, 4, 3)
    # print(b.board[4][5].getPossibleMoves(b.board))
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

    # b.movePieceFast(7, 5, 5, 5)
    # b.movePieceFast(7, 6, 5, 6)
    # b.movePieceFast(7, 3, 5, 3)
    # b.movePieceFast(7, 2, 5, 2)
    # b.movePieceFast(7, 1, 5, 1)
    # b.movePieceFast(6, 5, 4, 5)
    # b.movePieceFast(7, 4, 3, 3)
    # # b.generate_possible_moves("white", [0, 0, 0, 0])
    # print(b.board[3][3].getPossibleMoves(b.board))
    # b.printBoardWhite()

    # for i in range(8):
    #     for j in range(8):
    #         piece = b.board[i][j]
    #         if piece != "noPiece" and piece.color == "black":
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
    # b.movePieceFast(7, 5, 5, 5)
    # b.movePieceFast(7, 6, 5, 6)
    # b.movePieceFast(7, 3, 5, 3)
    # b.movePieceFast(7, 2, 5, 2)
    # b.movePieceFast(7, 1, 5, 1)
    # # b.generate_possible_moves("white", [0, 0, 0, 0])
    # print(b.board[7][7].getPossibleMoves(b.board))  #BUG FOUND HERE, SOLVED
    # b.printBoardWhite()

    """En Passant test Come back to this"""
    # b.movePieceFast(1, 5, 4, 5)
    # b.movePieceFast(6, 6, 4, 6)
    # print(b.board[4][5].color)
    # print(b.board[4][6].color)
    # b.board[4][6].enpassant = True
    # print(b.board[4][5].getPossibleMoves(b.board))



    # print("Is the king in check?", b.isCheck("white"))
    # b.printBoardWhite()

    # print(b.getLegalMoves("white"))

    # l = b.generate_possible_moves("white", [6, 4, 4, 4])
    # b.printBoardWhite()
    # print(len(l))
    # for move in l:
    #     fx = move[0]
    #     fy = move[1]
    #     tx = move[2]
    #     ty = move[3]
    #     piece = b.board[fx][fy]
    #     print(piece.color + piece.rep,"at", "%d,%d" % (fx, fy),"attempting to move to", "%d,%d" % (tx, ty))

    ## big test
    color = "white"
    l = b.generate_possible_moves(color, [6, 4, 4, 4])
    movecount = 1

    while (len(l) != 0):
        total_pieces = 0
        for i in range(8):
            for j in range(8):
                if not b.isSquareEmpty(i, j):
                    total_pieces += 1
        print(total_pieces)
        if total_pieces == 2:
            break
        move = random.choice(l)
        fx = move[0]
        fy = move[1]
        tx = move[2]
        ty = move[3]
        piece = b.board[fx][fy]
        if not b.isSquareEmpty(tx, ty):
            epiece = b.board[tx][ty]
            print(str(movecount)+".", piece.color + piece.rep, "at", "%d,%d" % (fx, fy), "attempting to take the", epiece.color+epiece.rep, "at %d,%d" % (tx, ty))
        else:
            print(str(movecount)+".", piece.color + piece.rep,"at", "%d,%d" % (fx, fy),"attempting to move to", "%d,%d" % (tx, ty))
        if color == "white":
            color = "black"
        else:
            color = "white"
        l = b.generate_possible_moves(color, move)
        b.printBoardWhite()
        movecount += 1
        # time.sleep(1)
    print("GameOver!")





