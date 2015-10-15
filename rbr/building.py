"""building.py: This file describe a building object, a building basically is a room holding doors"""

from random import randint, choice

__author__ = 'lplume'
__credits__ = ['dario p']
__license__ = 'Do the fuck you want public license'


class Building:
    def __init__(self):
        self.tlx = None
        self.tly = None
        self.brx = None
        self.bry = None
        self.width = None
        self.height = None
        self.empty_walls = None

    def getCoord(self):
        return self.tlx, self.tly, self.brx, self.bry

    def getTopCoord(self):
        return self.tlx, self.tly

    def getBottomCoord(self):
        return self.brx, self.bry

    def getDimension(self):
        return self.width, self.height

    def getEmptyWalls(self):
        return self.empty_walls

    def buildAround(self, door, wall, width=0, height=0):
        building_type = choice(['r', 'h'])
        if building_type == 'r':
            return self.createRoom(door, wall, width, height)
        else:
            return self.createHalliway(door, wall)

    def createHalliway(self, door, wall):
        if wall == 'n' or wall == 's':
            width = 3  # randint(3, 5)
            height = width * randint(2, 3)
        if wall == 'w' or wall == 'e':
            height = 3  # randint(3, 5)
            width = height * randint(2, 3)

        return self.createRoom(door, wall, width, height)

    def createRoom(self, door, wall, width, height):
        self.width, self.height = width, height

        door_x, door_y = door.getCoord()
        if wall == 'n':
            self.tly = door_y + 1
            self.tlx = randint(door_x - width + 1, door_x)
            self.empty_walls = ['e', 'w', 's']
        elif wall == 's':
            self.tly = door_y - height
            self.tlx = randint(door_x - width + 1, door_x)
            self.empty_walls = ['w', 'n', 'e']
        elif wall == 'e':
            self.tlx = door_x - width
            self.tly = randint(door_y - height + 1, door_y)
            self.empty_walls = ['s', 'w', 'n']
        elif wall == 'w':
            self.tlx = door_x + 1
            self.tly = randint(door_y - height + 1, door_y)
            self.empty_walls = ['n', 'e', 's']

        self.brx = self.tlx + width
        self.bry = self.tly + height

        return self
