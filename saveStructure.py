from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import pickle

# Program copies a strcture like a building in minecraft and saves it in a file

def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    height = y2 - y1
    width = x2 - x1
    length = z2 - z1

    structure = []

    for row in range(height):
        structure.append([])
        for column in range(width):
            structure[row].append([])
            for depth in range(length):
                block = mc.getBlockWithData(x1 + column, y1 + row, z1 + depth)
                structure[row][column].append(block)

    return structure

# Get the position of the first corner
input("Move to a corner and press ENTER!")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Move to the opposite corner and press ENTER!")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

print("Please wait copy structure!")

structure = copyStructure(x1, y1, z1, x2, y2, z2)

# Store the structure in a file
try:
    with open("my_structure.txt", "wb") as fh:
        pickle.dump(structure, fh)
        print("Structure was successfully copied and saved too " + fh.name)
except:
    print("An ERROR occured! Could not open file!")
