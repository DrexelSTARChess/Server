from flask import Flask, escape, request, jsonify
import time

from board import *
from boardTranslator import clientToServer, serverToClient
from helper import player_num_to_color, get_other_player_num
from player import Player

app = Flask(__name__)
player_count = 0
board = None
players = {1: None, 2: None}


@app.route('/startGame')
def start_game():
	global player_count
	global board

	# Server is full, cannot accept new players
	if player_count >= 2:
		return jsonify({"status_code": 503})

	# Player has connected, board created
	player_count += 1
	if player_count == 1:
		players[1] = Player("white")
		board = Board()
	else:
		players[2] = Player("black")

	return jsonify({"status_code": 200, "player": player_count, "color": players[player_count].color})


@app.route('/quitGame')
def quit_game():
	return


@app.route('/waitForPlayer')
def wait_for_player():
	global player_count
	arguments = request.get_json()
	player_number = arguments["player_number"]

	while player_count < 2:
		time.sleep(0.5)

	return jsonify(
				{
					"status_code": 200,
					"boardData": serverToClient(board),
					"moveData": board.generateMoves(player_num_to_color[player_number])
				}
			)


@app.route('/waitForTurn')
def wait_for_turn():
	global board

	arguments = request.get_json()
	player_number = arguments["player_number"]
	current_player = players[player_number]
	# Check if current_player has won
	if current_player.has_won:
		return jsonify(
			{
				"status_code": 200,
				"board_data": serverToClient(board),
				"move_data": [],
				"won": True,
				"lost": False
			}
		)

	# Wait other player's turn to end
	while current_player.is_turn == False:
		time.sleep(0.5)

	# If game is over, then this player has lost
	moves = board.generateMoves(current_player.color)
	if moves is []:
		current_player.has_lost = True
		players[get_other_player_num(player_number)].has_won = True
		return jsonify(
			{
				"status_code": 200,
				"board_data": serverToClient(board),
				"move_data": [],
				"won": False,
				"lost": True,
			}
		)

	# Nobody has won, so continue the game
	return jsonify(
		{
			"status_code": 200,
			"board_data": serverToClient(board),
			"move_data": moves,
			"won": False,
			"lost": False
		}
	)


@app.route('/submitBoard')
def submit_board():
	global board
	# We need to let wait_for_turn know to move on

	arguments = request.get_json()
	player_number = arguments["player"]
	board.setBoard(clientToServer(arguments["board"]))

	# Switching players
	players[player_number].is_turn = False
	other_player_number = get_other_player_num(player_number)
	players[other_player_number].is_turn = True

	return jsonify(
				{
					"status_code": 200,
				}
			)
