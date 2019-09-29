from mcpi.minecraft import Minecraft
mc = Minecraft.create()

""" The script creates a wool wall of 3 block width and 5 blocks height. """

colors = [[i] * 3 for i in range(6)]  # Creats a list of 5 rows with 3 elements

# Get the position of the player
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

startingX = x  # Needed so the next row begins where the first row did

for row in colors:
    for color in row:
        mc.setBlock(x, y, z, 35, color)
        x += 1
    y += 1
    x = startingX
