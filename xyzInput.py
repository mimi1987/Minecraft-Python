# Connect ot Minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Input xyz coordinates.
x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))

# Set a new player position.
mc.player.setPos(x, y, z)
