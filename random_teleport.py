from mcpi.minecraft import Minecraft
from random import randint
from time import sleep

mc = Minecraft.create()



count = 1

while count < 10:
    x = randint(-1000, 1000)
    y = randint(10, 50)
    z = randint(-3000, 3000)
    mc.player.setTilePos(x, y, z)
    sleep(3)
    count += 1

message = "Die Schleife ist beendet"

mc.postToChat(message)
