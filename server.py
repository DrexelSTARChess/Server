from flask import Flask, escape, request
import ujson
import gameHandler

app = Flask(__name__)


@app.route('/startGame')
def start_game():
	return


@app.route('/quitGame')
def quit_game():
	return


@app.route('/waitForTurn')
def wait_for_turn():
	return


@app.route('/submitBoard')
def submit_board():
	return
