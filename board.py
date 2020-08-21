class Board:
	"""docstring for Board"""
	def __init__(self):
		self.board = [
	        ["blackRook", "blackKnight", "blackBishop", "blackQueen", "blackKing", "blackBishop", "blackKnight", "blackRook"],
	        ["blackPawn", "blackPawn", "blackPawn", "blackPawn", "blackPawn", "blackPawn", "blackPawn", "blackPawn"],
	        ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
	        ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
	        ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
	        ["noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece", "noPiece"],
	        ["whitePawn", "whitePawn", "whitePawn", "whitePawn", "whitePawn", "whitePawn", "whitePawn", "whitePawn"],
	        ["whiteRook", "whiteKnight", "whiteBishop", "whiteQueen", "whiteKing", "whiteBishop", "whiteKnight", "whiteRook"]
	    ]

	def setBoard(self, newBoard):
		"""
		Take a Board object and set the board
		newBoard: the new value board will be set to
		"""
		self.board = newBoard

	def getBoard(self):
		"""
		A board getter
		Return: the Board object
		"""
		return self.board

	def isSquareEmpty(self, x, y):
		"""
		Checks if any piece is in a specified coordinate
		x: the x coordinate to be checked
		y: the y coordinate to be checked
		Return: boolean representing result
		"""
		return False

	def isGameOver(self):
		return False

	def isCheck(self, playerColor):
		return False

	def quit(self, playerColor):
		return False
	
	def generateMoves(self, playerColor):
		return []
