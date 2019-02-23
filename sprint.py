# Connect to minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Make the programm wait
from time import sleep

sleep(2)

# Get the players current position.
pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

# Wait ten seconds.
sleep(10)

# Get second position.
pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

# Calculate the distance traveled.
xDistance = x2 - x1
yDistance = y2 - y1
zDistance = z2 - z1

# Post the traveled distance to the minecraft chat.
message = "I travelled x: " + str(xDistance) + ", y: " + str(yDistance) + ", z: " + str(zDistance)
mc.postToChat(message)
