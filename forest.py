from mcpi.minecraft import Minecraft
from random import randint
mc = Minecraft.create()

def growTree(x, y, z, tree):
    mc.setBlock(x, y, z, tree)


pos = mc.player.getTilePos()

x = pos.x + randint(1, 10)
y = pos.y
z = pos.z

tree = 6

growTree(x, y, z, tree)
