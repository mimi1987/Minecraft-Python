# Connect to minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Make the program wait
import time
time.sleep(5)

# Get players position.
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Create a air cube.
air = 0
mc.setBlocks(x, y, z, x + 20, y + 20, z + 20, air)
