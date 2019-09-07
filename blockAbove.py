from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 44

mc.setBlock(x, y , z + 1, blockType)

for i in range(5):
    mc.setBlock(x, y, z + i, blockType)
    mc.setBlock(x, y, z - i, blockType)
    mc.setBlock(x + i, y, z, blockType)
    mc.setBlock(x - i, y, z, blockType)
