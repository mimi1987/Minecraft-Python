from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

randomStructure = [[random.randint(0,4) for _ in range(10)] for _ in range(10)]

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

for row in randomStructure:
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = pos.x
