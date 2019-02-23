# Mit Minecraft verbinden.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# X, Y und Z Variablen für Koordinaten deklarieren.
x, y, z = -1283, 63, -1098

# Blocks.
blockBrick = 45
blockBookshelf = 47

# Block erstellen.
for i in range(1000):
    mc.setBlock(x, y, z, blockBrick)
    y += 1
    mc.setBlock(x, y, z, blockBookshelf)
