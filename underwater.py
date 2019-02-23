# Connect to Minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# My current position.
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Block under my feet.
blockTypeFeet = mc.getBlock(x, y, z)

# Block above my head.
blockTypeHead = mc.getBlock(x, y + 1, z)

# Find out if I am underwater.
water = 9

underwater = blockTypeFeet == water and blockTypeHead == water

# Post the answer to the minecraft chat.
message = "Am I underwater? " + str(underwater)
mc.postToChat(message)
