# Used to make the execution of code to wait.
from time import sleep

# Connect to minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Wait 5 seconds.
sleep(5)

# Post a message to the minecraft chat.
mc.postToChat("Hello Minecraft World!")

# Get players current position.
pos = mc.player.getTilePos()

# Assign x position and display it.
x = str(pos.x)
mc.postToChat("My current x position is: " + x)

# Post the type of block on which I am standing.
#blockType = mc.getBlock()
#mc.postToChat(blockType)
