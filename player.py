class Player:
    def __init__(self, color):
        self.is_turn = False
        self.color = color
        self.has_won = False
        self.has_lost = False
