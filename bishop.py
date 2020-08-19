from chessPiece import ChessPiece

class Bishop(ChessPiece):
	"""docstring for Bishop"""
	def __init__(self, color, x, y):
		super(Bishop, self).__init__(color, x, y)
	
	def getPossibleMoves(self, board):
		return [][]