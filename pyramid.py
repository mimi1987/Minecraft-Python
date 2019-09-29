from mcpi.minecraft import Minecraft
mc = Minecraft.create()

""" The script builds a pyramid out of a sandstone block. """

height = 10
levels = reversed(range(10))  # Pyramids are made up of levels
sandstone = 24  # Sandstone ID

# Get players position
pos = mc.player.getTilePos()
x, y, z = pos.x + 50, pos.y, pos.z  # That's a tuple expansion

# Creates the diffrent levels of the pyramid
for level in levels:
    mc.setBlocks(x - level, y, z - level, x + level, y, z + level, sandstone)
    y += 1
