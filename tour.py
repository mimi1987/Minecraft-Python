# Connect to Minecraft
from random import randint
from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set x, y and z variables to represent coordinates
x = -319.449
y = 63.000
z = 156.376

# Change the player's position
mc.player.setPos(x, y, z)


sleep(10)

x = -256.483
y = 62.47590
z = -414.085

mc.player.setPos(x, y, z)




