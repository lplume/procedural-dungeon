""" door.py: This object is just a door and it will be create on an empty building wall."""

from random import choice, randint

__author__ = 'lplume'
__license__ = 'Do the fuck you want public license'


class Door:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getCoord(self):
        return self.x, self.y

    def setCoord(self, x, y):
        self.x, self.y = x, y

    def createDoor(self, building):
        wall = choice(building.getEmptyWalls())
        build_top_x, build_top_y = building.getTopCoord()
        build_bottom_x, build_bottom_y = building.getBottomCoord()
        if wall == 'n':
            self.x = randint(build_top_x, build_bottom_x - 1)
            self.y = build_top_y - 1
            next_wall = 's'
        elif wall == 's':
            self.x = randint(build_top_x, build_bottom_x - 1)
            self.y = build_bottom_y
            next_wall = 'n'
        elif wall == 'w':
            self.x = build_top_x - 1
            self.y = randint(build_top_y, build_bottom_y - 1)
            next_wall = 'e'
        elif wall == 'e':
            self.x = build_bottom_x
            self.y = randint(build_top_y, build_bottom_y - 1)
            next_wall = 'w'

        return self, next_wall
