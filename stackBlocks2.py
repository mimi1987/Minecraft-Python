from mcpi.minecraft import Minecraft
mc = Minecraft.create()

""" The script builds a queue of wool blocks. """

colors = list(range(0,6))

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

for color in colors:
    mc.setBlock(x, y, z, 35, color)
    x += 1  # Stack grows horizontal
