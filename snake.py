from segment import Segment
from segmenttype import SegmentType
from field import Field


class Snake:
	def __init__(self, x, y, limitX, limitY):
		self.body = []
		self.body.append(Segment(SegmentType.snakeHead, limitX, limitY))
		self.body[0].setDirection(1)
		self.body[0].setXY(x, y)
		self.limitX = limitX
		self.limitY = limitY
		self.head = self.body[0]
		self.crashSubscribers = []
		self.blockDirChange = False


	def grow(self, n = 1):
		for i in range(n):
			(x, y) = self.body[-1].getXY()
			self.body.append(Segment(SegmentType.snakeBody, self.limitX, self.limitY))
			self.body[-1].setXY(x, y)


	def move(self):
		self.body[0].move()
		pos1 = self.body[0].getXY()
		happened = False

		for i in range(1, len(self.body)):
			pos2 = self.body[-i].getXY()

			# in case of crashing into itself
			if pos1 == pos2:
				self.crashEvent()
				break

			self.body[-i].move()
			# get previous segment direction
			self.body[-i].setDirection(self.body[-i-1].getDirection())

		self.blockDirChange = False
			


	def printToField(self, gameField):
		for i in range(1, len(self.body)+1):
			(x, y) = self.body[-i].getXY()
			gameField.printXY(x, y, self.body[-i].getType())


	def getHeadPos(self):
		return self.body[0].getXY()


	def setDirection(self, newDirection):
		if self.blockDirChange == False:
			self.body[0].setDirection(newDirection)

			# żeby nie można było się cofnąć w swoje ciało
			self.blockDirChange = True
  

	def subscribeToCrashEvent(self, eventHandler):
		self.crashSubscribers.append(eventHandler)


	def crashEvent(self):
		for subscriber in self.crashSubscribers:
			subscriber()

