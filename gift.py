from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 1300
y = 82
z = 52

diamond = 57
tree_sapling = 6
air = 0

mc.setBlock(x, y, z, tree_sapling)

if mc.getBlock(x, y, z) == diamond:
    mc.postToChat("Thanks for the diamond.")
elif mc.getBlock(x, y, z) == tree_sapling:
    mc.postToChat("I guess tree saplings are as good as diamonds.")
else:
    mc.postToChat("Bring a gift to " + str(x) + ", " + str(y) + ", " + str(z))

