from math import floor
import math
import time
import random
import os
import threading
import math

from segmenttype import SegmentType
from screen import ScreenBuffer
from field import Field
from snake import Snake
from segment import Segment

class Game:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.snek = Snake(math.floor(x/2)-1, math.floor(y/2), x, y)
		self.gameField = Field(x, y)
		self.buffer = ScreenBuffer()
		self.snack = Segment(SegmentType.snack)
		self.newSnack()
		self.gameOver = False
		self.score = 0
		self.newDirection = None


	def startGame(self):
		self.snek.grow()
		self.snek.grow()
		thread = threading.Thread(target=self.gameLoop, args=())
		thread.daemon = True
		thread.start()
		self.readInput()


	def gameLoop(self):
		while self.gameOver == False:
			(x, y) = self.snek.getHeadPos()
			(x2, y2) = self.snack.getXY()

			self.gameField.clean()
			self.gameField.printXY(x2, y2, self.snack.getType())
			self.snek.printToField(self.gameField)
			self.buffer.printToConsole(self.gameField.toString(), True)
			self.buffer.printToConsole("\n Wynik: " + str(self.score))
			self.buffer.printLegend()

			time.sleep(0.15)

			self.snek.move()

			if (x == x2 and y == y2):
				self.snek.grow()
				self.newSnack()
				self.score += 1


	def newSnack(self):
		newX = random.randint(0, self.x -1)
		newY = random.randint(0, self.y -1)
		self.snack.setXY(newX, newY)


	def end(self):
		self.gameOver = True
		self.buffer.clrscr()
		self.buffer.printToConsole("\n Wynik: " + str(self.score))
		self.buffer.printToConsole(" Gratulacje!")


	def readInput(self):
		result = None

		while self.gameOver == False:
			if os.name == "nt":
				import msvcrt
				result = msvcrt.getch();
			else:
				result = os.popen("""bash -c 'read -rsn 1 BOBO && printf $BOBO'""").read()

			if result == "w":
				self.snek.setDirection(0)
			elif result == "d":
				self.snek.setDirection(1)
			elif result == "s":
				self.snek.setDirection(2)
			elif result == "a":
				self.snek.setDirection(3)
			elif result == "p":
				self.end()
