from mcpi.minecraft import Minecraft
mc = Minecraft.create()

""" Script draws a smiley. """

# List holds the information for the pixel art
smiley = [[35, 35, 22, 22, 22, 22, 35, 35],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 35, 35, 35, 35, 22],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 22, 22, 35, 35, 22],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [35, 35, 22, 22, 22, 22, 35, 35]]

# Get players current position
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

# Two for loops to create the two dimensional form
for row in reversed(smiley):  # Reverse so bottom of list is bottom of the pixel art
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = pos.x
    
