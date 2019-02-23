# Connect to Minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Get the current player position.
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z + 1

# Create a block.
try:
    blockType = int(input("Which block do you want to create? "))
    mc.setBlock(x, y, z, blockType)
except:
    print("Please enter the number of the block you wish to create.")
    
