import PIL
import configparser, pprint

__author__ = 'mauro'

class Dungeon:

    def __init__(self, cols = 10, rows = 10):
        self.cols = cols
        self.rows = rows
        self.dungeon = [['#' for x in range(cols)] for y in range(rows)]
        self.doors = []
        self.buildings = []
        self.config = configparser.ConfigParser()
        self.config.read('config.sample.ini')
        self.minx, self.miny, self.maxx, self.maxy = 0, 0, 0, 0


    def getDimension(self):
        return self.cols, self.rows

    def getDungeon(self):
        return self.dungeon

    def getDoors(self):
        return self.doors

    def addDoor(self, door):
        x, y = door.getCoord()
        if x < self.minx: self.minx = x
        if x > self.maxx: self.maxx = x
        if y < self.miny: self.miny = y
        if y > self.maxy: self.maxy = y
        self.doors.append(door)

    def getBuildings(self):
        return self.buildings

    def addBuilding(self, building):
        tx, ty, bx, by = building.getCoord()
        if tx < self.minx: self.minx = tx
        if tx > self.maxx: self.maxx = tx
        if ty < self.miny: self.miny = ty
        if ty > self.maxy: self.maxy = ty
        if bx < self.minx: self.minx = bx
        if bx > self.maxx: self.maxx = bx
        if by < self.miny: self.miny = by
        if by > self.maxy: self.maxy = by
        self.buildings.append(building)

    def print(self):
        pprint.pprint(self.config['DUNGEON']['tileset'])
         # for d in self.doors:
         #     door_x, door_y = d.getCoord()
         #     self.dungeon[door_y][door_x] = 'D'
         #
         # for b in self.buildings:
         #     x, y = b.getTopCoord()
         #     w, h = b.getDimension()
         #     for row in range(y, y + h):
         #         for col in range(x, x + w):
         #             self.dungeon[row][col] = ' '
         #
         # for row in range(0, self.rows):
         #     for col in range(0, self.cols):
         #         print(self.dungeon[row][col], end="")
         #
         #     print()