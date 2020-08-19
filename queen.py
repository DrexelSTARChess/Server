from chessPiece import ChessPiece

class Queen(ChessPiece):
	"""docstring for Queen"""
	def __init__(self, color, x, y):
		super(Queen, self).__init__(color, x, y)
	
	def getPossibleMoves(self, board):
		return [][]