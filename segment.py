class Segment:

	def __init__(self, initType, limitX = 1, limitY = 1):
		self.x = 0
		self.y = 0
		self.limitX = limitX
		self.limitY = limitY
		self.type = initType
		self.direction = 4

	def setX(self, newX):
		self.x = newX

	def setY(self, newY):
		self.y = newY

	def setXY(self, newX, newY):
		self.setX(newX)
		self.setY(newY)

	def getXY (self):
		return (self.x, self.y)

	def getType(self):
		return self.type

	def setDirection(self, newDirection):
		self.direction = newDirection

	def getDirection(self):
		return self.direction

	def move(self):
		if self.direction == 0:
			self.y -= 1

		elif self.direction == 1:
			self.x += 1

		elif self.direction == 2:
			self.y += 1

		elif self.direction == 3:
			self.x -= 1

		self.x = self.x % self.limitX
		self.y = self.y % self.limitY

