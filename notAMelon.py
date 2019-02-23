from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 1
z = 20

melon = 103
mc.setBlock(x, y, z, melon)

block = mc.getBlock(x + 2, y, z)

noMelon = not (block == melon)

mc.postToChat("I need to get some food: " + str(noMelon))


