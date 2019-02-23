# Connect to Minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Get the blocktype from the player.
blockType = int(input("Which blocktype do you want to create? "))

# Get the current player position.
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Create cube.
mc.setBlocks(x + 1, y, z + 1, x + 13, y + 12, z + 13, blockType)
mc.setBlocks(x + 2, y + 1, z + 2, y + 12, y + 11, z + 12, 0)
