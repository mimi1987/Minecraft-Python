# Connect to minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# My position.
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# My block where I'm standing.
blockType = mc.getBlock(x, y - 1, z)


# Am I in a tree?
wood = 11
leaves = 18

inTree = blockType == wood or blockType == leaves


# Post to chat.
message = "Am i in a tree? " + str(inTree)

mc.postToChat(message)

