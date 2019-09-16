from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

blocks = [20] * 10 # Makes a list of ten twenties.
barBlock = 22 # Lapis lazuli

count = 0
while count <= len(blocks):
    for i in range(len(blocks)-1):
        mc.setBlock(x, y+i, z, blocks[i])

    count += 1

    del blocks[len(blocks)-1]

    blocks.insert(0, barBlock)

    time.sleep(1)
