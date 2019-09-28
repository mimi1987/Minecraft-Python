from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

stairBlock = 53

for stair in range(10000):
    mc.setBlock(x+stair, y+stair, z, stairBlock)
    
