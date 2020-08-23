from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import time

from board import Board
from boardTranslator import server_to_client
from helper import player_num_to_color, get_other_player_num
from player import Player

app = Flask(__name__)
CORS(app)

player_count = 0
board = None
players = {1: None, 2: None}


def restart_vars():
    global player_count
    global board
    global players

    player_count = 0
    board = None
    players[1] = None
    players[2] = None


@app.route('/startGame', methods=['GET', 'POST'])
@cross_origin()
def start_game():
    global player_count
    global board

    # Reset if player_count goes to 0
    if player_count <= 0:
        restart_vars()

    # Server is full, cannot accept new players
    if player_count >= 2:
        return jsonify({"status_code": 503})

    # Player has connected, board created
    player_count += 1
    if player_count == 1:
        players[1] = Player("white")
        players[1].is_turn = True
        board = Board()
    else:
        players[2] = Player("black")

    return jsonify(
        {
            "status_code": 200,
            "player_number": player_count,
            "color": players[player_count].color
        }
    )


@app.route('/quitGame', methods=['GET', 'POST'])
@cross_origin()
def quit_game():
    global player_count
    arguments = request.get_json()

    # Setting attributes for quitting player
    quitting_player_num = arguments["player_number"]
    quitting_player = players[quitting_player_num]
    quitting_player.has_lost = True

    # Setting attributes for winning player
    winning_player_num = get_other_player_num(quitting_player_num)
    winning_player = players[winning_player_num]
    if winning_player is not None:
        winning_player.has_won = True

    player_count -= 1

    return jsonify(
        {
            "status_code": 200,
            "board_data": server_to_client(board),
            "move_data": [],
            "won": False,
            "lost": True,
        }
    )


@app.route('/waitForPlayer', methods=['GET', 'POST'])
@cross_origin()
def wait_for_player():
    global player_count
    arguments = request.get_json()
    player_number = arguments["player_number"]

    while player_count < 2:
        if players[player_number].has_lost:
            player_count -= 1
            return jsonify(
                {
                    "status_code": 200,
                    "board_data": server_to_client(board),
                    "move_data": [],
                    "won": False,
                    "lost": True,
                }
            )

        time.sleep(0.5)

    return jsonify(
                {
                    "status_code": 200,
                    "board_data": server_to_client(board),
                    "move_data": board.getLegalMoves(
                        player_num_to_color[player_number]
                    ),
                    "won": False,
                    "lost": False
                }
            )


@app.route('/waitForTurn', methods=['GET', 'POST'])
@cross_origin()
def wait_for_turn():
    global board
    global player_count

    arguments = request.get_json()
    player_number = arguments["player_number"]
    waiting_player = players[player_number]
    # Wait for other player's turn to end or for someone to forfeit
    while not waiting_player.is_turn and\
            not waiting_player.has_lost and\
            not waiting_player.has_won:
        time.sleep(0.5)

    # Check if waiting_player has won
    if waiting_player.has_won:
        player_count -= 1
        return jsonify(
            {
                "status_code": 200,
                "board_data": server_to_client(board),
                "move_data": [],
                "won": True,
                "lost": False,
                "draw": False,
                "is_check": board.isCheck(players[player_number].color)
            }
        )

    # If game is over, then this player has lost; If draw then neither wins
    moves = board.getLegalMoves(waiting_player.color)
    if moves is [] or waiting_player.has_lost:
        is_draw = False
        if board.getWinner() == "draw":
            is_draw = True
        else:
            waiting_player.has_lost = True
            # Making sure the other player is initialized
            other_player_num = get_other_player_num(player_number)
            other_player = players[other_player_num]
            if other_player:
                players[get_other_player_num(player_number)].has_won = True

        player_count -= 1
        return jsonify(
            {
                "status_code": 200,
                "board_data": server_to_client(board),
                "move_data": [],
                "won": False,
                "lost": waiting_player.has_lost,
                "draw": is_draw,
                "is_check": board.isCheck(players[player_number].color)
            }
        )

    # Nobody has won, so continue the game
    return jsonify(
        {
            "status_code": 200,
            "board_data": server_to_client(board),
            "move_data": moves,
            "won": False,
            "lost": False,
            "draw": False,
            "is_check": board.isCheck(players[player_number].color)
        }
    )


@app.route('/submitBoard', methods=['GET', 'POST'])
@cross_origin()
def submit_board():
    global board
    # We need to let wait_for_turn know to move on

    arguments = request.get_json()
    player_number = arguments["player_number"]
    player_move = arguments["player_move"]
    board.applyMove(players[player_number].color, player_move)

    # Switching players
    players[player_number].is_turn = False
    other_player_number = get_other_player_num(player_number)
    players[other_player_number].is_turn = True

    return jsonify(
                {
                    "status_code": 200,
                    "board_data": server_to_client(board)
                }
            )
