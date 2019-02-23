# Connect to Minecraft
from random import randint
from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set x, y and z variables to represent coordinates
x = randint(1, 100)
y = randint(1, 100)
z = randint(1, 100)

a, b, c = 300, 69, 60

# Change the player's position
mc.player.setTilePos(x, y, z)

sleep(3)

mc.player.setTilePos(a, b, c)



