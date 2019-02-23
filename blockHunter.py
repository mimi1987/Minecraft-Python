from mcpi.minecraft import Minecraft
from math import sqrt
from random import randint

mc = Minecraft.create()

dest = mc.player.getTilePos()

destX = dest.x
destZ = dest.z + 5
destY = mc.getHeight(destX, destZ)

block = 57
mc.setBlock(destX, destY, destZ, block)
mc.postToChat("Block set")

while True:
    pos = mc.player.getTilePos()
    distance = sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)

    if distance > 100:
        mc.postToChat("Freezing")
    elif distance > 50:
        mc.postToChat("Cold")
    elif distance > 25:
        mc.postToChat("Warm")
    elif distance > 12:
        mc.postToChat("Boiling")
    elif distance > 6:
        mc.postToChat("On fire!")
    elif distance == 0:
        mc.postToChat("Found it")
        break
