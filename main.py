#! /usr/bin/python

from game import Game

print(" Podaj wielkość pola gry")
x = int(input(" x: "))
y = int(input(" y: "))

if x < 6:
	x = 6

if y < 6:
	y = 6

# hide terminal cursor
print("\033[?25l")

gam = Game(x, y)
try:
	gam.startGame()
except:
	gam.end()

# show terminal cursor
print("\033[?25h")
