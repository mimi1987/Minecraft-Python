from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

# Get the player's position
pos = mc.player.getTilePos()

# Set the x, y and z variables on the same line using a tuple
x, y, z = pos.x, pos.y, pos.z

while True:
    x += random.uniform(-0.2, 0.2)
    # Change the z variable by a random float
    z += random.uniform(-0.2, 0.2)
    y = mc.getHeight(x, z)

    mc.player.setPos(x, y, z)
    time.sleep(0.1)
