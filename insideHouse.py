from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x, y, z, x + 6, y + 5, z + 12, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + 5, y + 4, z + 11, 0)

