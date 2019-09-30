from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Get players position
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

# Cube building data
cube = [[[57, 57, 57, 57],
         [57, 0, 0, 57],
         [57, 0, 0, 57],
         [57, 57, 57, 57]],
        #
        [[57, 0, 0, 57],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [57, 0, 0, 57]],
        #
        [[57, 0, 0, 57],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [57, 0, 0, 57]],
        #
        [[57, 57, 57, 57],
         [57, 0, 0, 57],
         [57, 0, 0, 57],
         [57, 57, 57, 57]]]

startingX = x
startingY = y

for depth in cube:
    for height in depth:
        for block in height:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = startingX
    z += 1
    y = startingY
