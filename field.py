from segmenttype import SegmentType

class Field:
    def __init__(self, x, y):
        self.gameField = None
        self.x = x
        self.y = y
        self.clean()


    def printXY(self, x, y, toPrint):
        self.gameField[y % self.y][x % self.x] = toPrint


    def clean(self):
        self.gameField = [["  " for i in range(self.x)] for j in range(self.y)]


    def toString(self):
        out = ""

        for i in range(self.x+2):
            out += SegmentType.wall

        out += "\n"

        for i in range(self.y):
            out += SegmentType.wall
            for j in range(self.x):
                out = out + self.gameField[i][j]
            out += SegmentType.wall + "\n"

        for i in range(self.x+2):
            out += SegmentType.wall

        return out
