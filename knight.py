from chessPiece import ChessPiece

class Knight(ChessPiece):
	"""docstring for Knight"""
	def __init__(self, color, x, y):
		super(Knight, self).__init__(color, x, y)
	
	def getPossibleMoves(self, board):
		return [][]