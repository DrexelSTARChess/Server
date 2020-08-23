from unittest import TestCase
from server import app, restart_vars


class TestIntegrations(TestCase):
    def setUp(self):
        self.client1 = app.test_client()
        self.client2 = app.test_client()
        self.client3 = app.test_client()

    def tearDown(self):
        restart_vars()

    def test_start_game(self):
        response = self.client1.post("/startGame")
        assert response.json["player_number"] == 1
        response_two = self.client2.post("/startGame")
        assert response_two.json["player_number"] == 2
        response_three = self.client3.post("/startGame")
        assert response_three.json["status_code"] == 503

    def test_submit_board(self):
        self.client1.post("/startGame")
        self.client2.post("/startGame")
        response = self.client1.post('/submitBoard', json={
            "player_number": 1,
            "player_move": [6, 0, 5, 0],
        })
        assert response.json["status_code"] == 200
        expected_board = [
            ['blackRook', 'blackKnight', 'blackBishop', 'blackQueen',
             'blackKing', 'blackBishop', 'blackKnight', 'blackRook'],
            ['blackPawn', 'blackPawn', 'blackPawn', 'blackPawn',
             'blackPawn', 'blackPawn', 'blackPawn', 'blackPawn'],
            ['noPiece', 'noPiece', 'noPiece', 'noPiece',
             'noPiece', 'noPiece', 'noPiece', 'noPiece'],
            ['noPiece', 'noPiece', 'noPiece', 'noPiece',
             'noPiece', 'noPiece', 'noPiece', 'noPiece'],
            ['noPiece', 'noPiece', 'noPiece', 'noPiece',
             'noPiece', 'noPiece', 'noPiece', 'noPiece'],
            ['whitePawn', 'noPiece', 'noPiece', 'noPiece',
             'noPiece', 'noPiece', 'noPiece', 'noPiece'],
            ['noPiece', 'whitePawn', 'whitePawn', 'whitePawn',
             'whitePawn', 'whitePawn', 'whitePawn', 'whitePawn'],
            ['whiteRook', 'whiteKnight', 'whiteBishop', 'whiteQueen',
             'whiteKing', 'whiteBishop', 'whiteKnight', 'whiteRook']
        ]
        board = response.json["board_data"]
        assert expected_board == board

    def test_quit_game(self):
        self.client1.post("/startGame")
        self.client2.post("/startGame")
        response = self.client1.post("/quitGame", json={"player_number": 1})
        response_json = response.json
        assert response_json["status_code"] == 200
        assert response_json["board_data"] == [
            ['blackRook', 'blackKnight', 'blackBishop', 'blackQueen',
             'blackKing', 'blackBishop', 'blackKnight', 'blackRook'],
            ['blackPawn', 'blackPawn', 'blackPawn', 'blackPawn',
             'blackPawn', 'blackPawn', 'blackPawn', 'blackPawn'],
            ['noPiece', 'noPiece', 'noPiece', 'noPiece',
             'noPiece', 'noPiece', 'noPiece', 'noPiece'],
            ['noPiece', 'noPiece', 'noPiece', 'noPiece',
             'noPiece', 'noPiece', 'noPiece', 'noPiece'],
            ['noPiece', 'noPiece', 'noPiece', 'noPiece',
             'noPiece', 'noPiece', 'noPiece', 'noPiece'],
            ['noPiece', 'noPiece', 'noPiece', 'noPiece',
             'noPiece', 'noPiece', 'noPiece', 'noPiece'],
            ['whitePawn', 'whitePawn', 'whitePawn', 'whitePawn',
             'whitePawn', 'whitePawn', 'whitePawn', 'whitePawn'],
            ['whiteRook', 'whiteKnight', 'whiteBishop', 'whiteQueen',
             'whiteKing', 'whiteBishop', 'whiteKnight', 'whiteRook']
        ]
        assert response_json["won"] is False
        assert response_json["lost"] is True
