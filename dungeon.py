__author__ = 'mauro'

class Dungeon:

    def __init__(self, cols = 10, rows = 10):
        self.cols = cols
        self.rows = rows
        self.dungeon = [['#' for x in range(cols)] for y in range(rows)]
        self.doors = []
        self.buildings = []

    def getDimension(self):
        return self.cols, self.rows

    def getDungeon(self):
        return self.dungeon

    def getDoors(self):
        return self.doors

    def addDoor(self, door):
        self.doors.append(door)

    def getBuildings(self):
        return self.buildings

    def addBuilding(self, building):
        self.buildings.append(building)

    def print(self):
         for d in self.doors:
             door_x, door_y = d.getCoord()
             self.dungeon[door_y][door_x] = 'D'

         for b in self.buildings:
             x, y = b.getTopCoord()
             w, h = b.getDimension()
             for row in range(y, y + h):
                 for col in range(x, x + w):
                     self.dungeon[row][col] = ' '

         for row in range(0, self.rows):
             for col in range(0, self.cols):
                 print(self.dungeon[row][col], end="")

             print()