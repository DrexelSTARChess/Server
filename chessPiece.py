from abc import ABC

class ChessPiece(ABC):
	"""docstring for ChessPiece"""
	def __init__(self, color, x, y):
		self.color = color
		self.x = x
		self.y = y

	def getPossibleMoves(self, board):
		return [][]

	def getPosition(self)
		return (x, y)

	def setPosition(self, x, y)
		self.x = x
		self.y = y

	def getColor(self):
		return self.color
