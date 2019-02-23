# Connect to minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Get players current position.
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

# Get block type.
blockType = mc.getBlock(x, y, z)

#Post to chat True equals water, False is everything else.
mc.postToChat(blockType == 9)
