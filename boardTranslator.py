from board import Board
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn


def client_to_server(board):
    """
    Translates client format of board to server format
    board: A 2D array of strings representing the board
    Returns: A 2D array of chess piece objects representing the board
    """
    result = [["noPiece" for i in range(8)] for j in range(8)]
    for row_num in range(0, len(board)):
        for column_num in range(0, len(board[row_num])):
            # Skip if
            if board[row_num][column_num] == "noPiece":
                continue

            first_char = board[row_num][column_num][:1]

            # Set piece color
            piece_color = "white"
            if first_char == "b":
                piece_color = "black"

            # Create each
            piece_type = board[row_num][column_num][5:]
            if piece_type == "Rook":
                result[row_num][column_num] = Rook(piece_color, row_num, column_num)
            elif piece_type == "Knight":
                result[row_num][column_num] = Knight(piece_color, row_num, column_num)
            elif piece_type == "Bishop":
                result[row_num][column_num] = Bishop(piece_color, row_num, column_num)
            elif piece_type == "Queen":
                result[row_num][column_num] = Queen(piece_color, row_num, column_num)
            elif piece_type == "King":
                result[row_num][column_num] = King(piece_color, row_num, column_num)
            elif piece_type == "Pawn":
                result[row_num][column_num] = Pawn(piece_color, row_num, column_num)

    return result


def server_to_client(board):
    """
    Translates server format of board to client format
    board: A 2D array of chess piece objects representing the board
    Returns: A 2D array of strings representing the board
    """
    result = [["noPiece" for i in range(8)] for j in range(8)]
    for row_num in range(0, len(board)):
        for column_num in range(0, len(board[row_num])):
            # Skip if noPiece
            if board[row_num][column_num] == "noPiece":
                continue

            piece_type = type(board[row_num][column_num])
            piece_string = board[row_num][column_num].getColor()

            # Create a string representation of each piece
            if piece_type is Rook:
                piece_string += "Rook"
            elif piece_type is Knight:
                piece_string += "Knight"
            elif piece_type is Bishop:
                piece_string += "Bishop"
            elif piece_type is Queen:
                piece_string += "Queen"
            elif piece_type is King:
                piece_string += "King"
            elif piece_type is Pawn:
                piece_string += "Pawn"

            result[row_num][column_num] = piece_string

    return result

# Some temp tests
if __name__ == "__main__":
    client_board = [
	        ["blackRook", "blackKnight", "blackBishop", "blackQueen", "blackKing", "blackBishop", "blackKnight", "blackRook"],
	        ["blackPawn", "blackPawn", "blackPawn", "blackPawn", "blackPawn", "blackPawn", "blackPawn", "blackPawn"],
	        ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
	        ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
	        ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
	        ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
	        ["whitePawn", "whitePawn", "whitePawn", "whitePawn", "whitePawn", "whitePawn", "whitePawn", "whitePawn"],
	        ["whiteRook", "whiteKnight", "whiteBishop", "whiteQueen", "whiteKing", "whiteBishop", "whiteKnight", "whiteRook"]
	    ]

    client_to_server_board = client_to_server(client_board)
    server_to_client_board = server_to_client(client_to_server_board)

    print("Do translations function correctly:", client_board == server_to_client_board)
