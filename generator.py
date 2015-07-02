#!/usr/bin/python3

from door import Door
from building import Building
from dungeon import Dungeon
import pprint, random


dungeon = Dungeon(100, 100)

for i in range(0, 20):
    if i == 0:
        door = Door(40,40)
        dungeon.addDoor(door)
        wall = random.choice(['n', 'e', 's', 'w'])
        building = Building().buildAround(door, wall, random.randint(3, 15), random.randint(3, 15))
        dungeon.addBuilding(building)
    door, wall = Door().createDoor(building)

    dungeon.addDoor(door)
    building = Building().buildAround(door, wall, random.randint(3, 15), random.randint(3, 15))
    dungeon.addBuilding(building)

dungeon.print()


