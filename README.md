# Server
This is the server component that manages games being played by the players.
It runs on Python 3 and Flask.
The server manages the game by storing a version of the game board that contains all of the piece positions,
and any relevant information on previous moves.
The server communicates between the two clients playing the game through end points and JSON objects.
This communication is used to organize player turns and handle legal move generation.

## Requirements
To run this server you need to have the following installed:
- Python 3
- Flask from pip3 (`pip3 install flask`)
- Flask-CORS from pip3 (`pip3 install flask-cors`)

Port `5000` must be available.

If you wish to access this server outside of your local network then you must open port `5000`.

## Running the Server
To run the server in development mode execute the following command in the root directory of this repository:

`env FLASK_APP=server.py flask run`

<hr/>
If you wish to make the development version accessible to devices other than the server
 run the following (doing this with a dev instance is **not recommended**):

`env FLASK_APP=server.py flask run --host=0.0.0.0`

It is a much better practice to
[run the server in production](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/)
to make it accessible to other devices.

## Using the Endpoints
Many endpoints are used by the client and server to communicate with one another.

| Endpoint      | Function                                                                                                                                                                      |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| startGame     | Creates a new game if there isn't one already looking for a player.                                                                                                           |
| waitForPlayer | Use this endpoint after using `startGame`.This waits until two players have joined then starts a game.                                                                       |
| submitBoard   | When a player makes a move this endpoint is used to send the updated board and the move made. The board stored in the server is then updated and sent to the opposing player. |
| waitForTurn   | Use this endpoint after making a turn (or when starting the game as player 2). This waits until the opposing player makes a move, the returns the updated board.              |
| quitGame      | Ends the game prematurely and awards the opposing player as the winner.                                                                                                       |

#### Expected Input Values:
`startGame`:

```
{}
```

<hr>

`waitForPlayer`:

```
{ "player_number": Int (1 | 2) }
```

<hr>

`submitBoard`:

```
{
    "player_number": Int (1 | 2),
    "board": String[8][8],
    "player_move": [4]
}
```

<hr>

`waitForTurn`:

```
{ "player_number": Int (1 | 2) }
```

<hr>

`quitGame`:

```
{ "player_number": Int (1 | 2) }
```

#### Return JSON

`startGame`:

```
{
    "status_code": 200,
    "player_number": Int (1 | 2),
    "color": String ("white" | "black")
}
```
Or if game could not be started because server is full:

```{"status_code": 503}```

<hr>

`waitForPlayer`:

```
{
    "status_code": 200,
    "board_data": String[8][8],
    "move_data": JSON[],
    "won": Boolean,
    "lost": Boolean
}
```

<hr>

`submitBoard`:

```
{ "status_code": 200 }
```

<hr>

`waitForTurn`:

```
{
    "status_code": 200,
    "board_data": String[8][8],
    "move_data": JSON[],
    "won": Boolean,
    "lost": Boolean,
    "is_check": Boolean
}
```

<hr>

`quitGame`:

```
{
    "status_code": 200,
    "board_data": String[8][8],
    "move_data": JSON[],
    "won": False,
    "lost": True
}
```

