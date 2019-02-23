from random import randint
from time import sleep
from mcpi.minecraft import Minecraft

# Mit Minecraft verbinden
mc = Minecraft.create()

# Variablen für die Spielerposition
x = randint(-100, 100)
y = randint(-100, 100)
z = randint(-100, 100)

# Spieler springt 10 mal herum
for i in range(10):
    mc.player.setTilePos(x, y, z)
    sleep(5)

