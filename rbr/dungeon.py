"""dungeon.py: this object is a doungeon holding buildings, doors and a fancy printable method (text and png)"""

from PIL import Image
import configparser, pprint

__author__ = 'lplume'
__credits__ = ['dario']
__license__ = 'Do the fuck you want public license'


class Dungeon:
    def __init__(self, cols=10, rows=10):
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
        tileset = Image.open(self.config['DUNGEON']['tileset'])
        tilesize = self.config.getint('DUNGEON', 'tilesize')

        width, height = (abs(self.minx) + self.maxx + 1) * tilesize, (abs(self.miny) + self.maxy + 1) * tilesize
        pprint.pprint(('immagine', width, height))

        output = Image.new("RGB", (width, height), 'red')

        empty_box = self.config['DUNGEON']['empty'].split(',')
        tlx, tly = int(empty_box[0]) * tilesize, int(empty_box[1]) * tilesize
        brx, bry = tlx + tilesize, tly + tilesize
        empty = tileset.crop((tlx, tly, brx, bry))

        wall_box = self.config['DUNGEON']['wall'].split(',')
        tlx, tly = int(wall_box[0]) * tilesize, int(wall_box[1]) * tilesize
        brx, bry = tlx + tilesize, tly + tilesize
        wall = tileset.crop((tlx, tly, brx, bry))

        door_box = self.config['DUNGEON']['door'].split(',')
        tlx, tly = int(door_box[0]) * tilesize, int(door_box[1]) * tilesize
        brx, bry = tlx + tilesize, tly + tilesize
        door = tileset.crop((tlx, tly, brx, bry))

        floor_box = self.config['DUNGEON']['floor'].split(',')
        tlx, tly = int(floor_box[0]) * tilesize, int(floor_box[1]) * tilesize
        brx, bry = tlx + tilesize, tly + tilesize
        floor = tileset.crop((tlx, tly, brx, bry))

        # empty flood
        for i in range(0, width, tilesize):
            for j in range(0, height, tilesize):
                output.paste(empty, (i, j))

        for b in self.buildings:
            # width, height = b.getDimension()
            tlx, tly, brx, bry = b.getCoord()
            ttlx = tilesize * (tlx + abs(self.minx) - 1)
            tbrx = tilesize * (brx + abs(self.minx))
            ttly = tilesize * (tly + abs(self.miny) - 1)
            tbry = tilesize * (bry + abs(self.miny))
            pprint.pprint(('building top/bottom y', ttly, tbry))
            for x in range(ttlx, tbrx, tilesize):
                output.paste(wall, (x, ttly))
                output.paste(wall, (x, tbry))
            for y in range(ttly, tbry + 1, tilesize):
                output.paste(wall, (ttlx, y))
                output.paste(wall, (tbrx, y))

        # doors
        for d in self.doors:
            x, y = d.getCoord()
            tx = tilesize * (x + abs(self.minx))
            ty = tilesize * (y + abs(self.miny))
            pprint.pprint(('dor x, y', tx, ty))
            output.paste(door, (tx, ty))

        for b in self.buildings:
            # width, height = b.getDimension()
            tlx, tly, brx, bry = b.getCoord()
            ttlx = tilesize * (tlx + abs(self.minx))
            tbrx = tilesize * (brx + abs(self.minx))
            ttly = tilesize * (tly + abs(self.miny))
            tbry = tilesize * (bry + abs(self.miny))
            pprint.pprint(('building top/bottom y', ttly, tbry))
            for x in range(ttlx, tbrx, tilesize):
                for y in range(ttly, tbry, tilesize):
                    output.paste(floor, (x, y))

        output.save('../output/rbr.png')

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
