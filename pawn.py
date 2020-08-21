from chessPiece import ChessPiece

class Pawn(ChessPiece):
	"""docstring for Pawn"""
	def __init__(self, color, x, y):
		super(Pawn, self).__init__(color, x, y)
	
	def getPossibleMoves(self, board):
		return [][]