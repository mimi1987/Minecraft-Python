from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

score = 0

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

water = 8
flowingWater = 9
blockAbove = mc.getBlock(x, y + 2, z)

while blockAbove == water or blockAbove == flowingWater:
    sleep(1)
    pos = mc.player.getTilePos()
    blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
    score = score + 1
    mc.postToChat("Current score: " + str(score))

mc.postToChat("Final score: " + str(score))

if score > 6:
    finalPos = mc.player.getTilePos()
    time = 0
    while time < 10:
        sleep(1)
        mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5, finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
        time = time + 1
