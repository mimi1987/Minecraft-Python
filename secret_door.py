from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Create a building.
##x = 184
##y = 63
##z = 531
##
##mc.setBlocks(x, y, z, x + 6, y + 6, z + 10, 4)
##mc.setBlocks(x + 1, y + 1, z + 1, x + 5, y + 5, z + 9, 0)


# Open secret door.
gift = 57
block = mc.getBlock(188, 64, 530)

if block != gift:
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 10)
elif block == gift:
    mc.setBlock(187, 63, 531, 0)
    mc.setBlock(187, 64, 531, 0)
    mc.setBlock(187, 65, 531, 0)
else:
    mc.postToChat("Place an offering on the pedestal.")
    
