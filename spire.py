# Connect to minecraft.
from mcpi.minecraft import Minecraft

# Create a session.
mc = Minecraft.create()

# Get the player position.
pos = mc.player.getTilePos()

# Define x, y, z coordinates with current position.
x = pos.x
y = pos.y
z = pos.z

# Declare variables for calculations.
height = 2
sideHeight = height * 2
baseHeight = height - 1
spire = sideHeight * 2

# Block type.
blockType = 1

# Built the base.
mc.setBlocks(x + 1, y, z + 1, x + 3, y + baseHeight, z + 3, blockType)

# Built the middel part.
mc.setBlocks(x + 2, y + height, z + 2, x + 2, y + sideHeight, z + 2, blockType)

# Built the spire.
mc.setBlocks( x + 3, y + sideHeight, z + 3, x + 3, y + spire, z + 3, blockType)
