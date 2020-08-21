from flask import Flask, escape, request
import ujson
import gameHandler

app = Flask(__name__)


@app.route('/startGame')
def startGame():
    # gameHandler.startGame("test") ??
    return


@app.route('/quitGame')
def quitGame():
    return


@app.route('/waitForTurn')
def waitForTurn():
    return


@app.route('/submitBoard')
def submitBoard():
    return
