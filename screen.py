import os

class ScreenBuffer:
	def __init__(self):
		self.command = 'clear'
		if os.name in ('nt', 'dos'):
			self.command = 'cls'

	def clrscr(self):
		os.system(self.command)


	def printToConsole(self, toPrint, clearOK = False):
		if clearOK:
			self.clrscr()
		print(toPrint)


	def printLegend(self):
		print("\n Poruszanie: wsad")
		print(" Wyjście: p")
		print()
