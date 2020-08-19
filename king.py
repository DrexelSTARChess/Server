from chessPiece import ChessPiece

class King(ChessPiece):
	"""docstring for King"""
	def __init__(self, color, x, y):
		super(King, self).__init__(color, x, y)
	
	def getPossibleMoves(self, board):
		return [][]