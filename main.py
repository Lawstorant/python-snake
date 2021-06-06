#! /usr/bin/python

from game import Game

print(" Podaj wielkość pola gry")
x = int(input(" x: "))
y = int(input(" y: "))

if x < 9:
	x = 9

if y < 9:
	y = 9

# hide terminal cursor
print("\033[?25l")

gam = Game(x, y)
try:
	gam.startGame()
except:
	gam.end()

# show terminal cursor
print("\033[?25h")
