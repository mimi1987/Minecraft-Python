from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import pickle

def buildStructure(x, y, z, structure):
    startX = x
    startZ = z

    for row in structure:
        for column in row:
            for block in column:
                mc.setBlock(x, y, z, block.id, block.data)
                z += 1
            x += 1
            z = startZ
        y += 1
        x = startX

try:
    with open("my_structure.txt", "rb") as fh:
        structure = pickle.load(fh)
        pos = mc.player.getTilePos()
        x, y, z = pos.x, pos.y, pos.z
        buildStructure(x, y, z, structure)
        print("Successfully built the structure!")
except FileNotFoundError as error:
    print("ERROR! Could not load the file.")
    print(error)
