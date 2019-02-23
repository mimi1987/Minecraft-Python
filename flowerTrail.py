from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 38)
    sleep(0.2)
