from mcpi.minecraft import Minecraft
mc = Minecraft.create()

""" Script builds a stack of wool blocks in diffrent colors. """

colors = list(range(0,6))

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

for color in colors:
    mc.setBlock(x, y, z, 35, color)
    y += 1  # Stack grows upwards
