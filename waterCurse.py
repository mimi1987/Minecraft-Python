from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

count = 1

while count < 60:
    mc.setBlock(x, y, z, 8)
    count += 1
    sleep(0.5)

mc.postToChat("Flood has finished!")
