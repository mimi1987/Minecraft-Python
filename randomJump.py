# For random numbers.
from random import randint

# Connect to minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Get player position.
pos = mc.player.getTilePos()

# Assign the coordinates.
x = pos.x
y = pos.y
z = pos.z


# Assign random number.
x += randint(-10, 10)
y += randint(0, 10)
z += randint(-10, 10)

# Give player a random position.
mc.player.setPos(x, y, z)
