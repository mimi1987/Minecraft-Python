# Connect to Minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Sleep used to make the programm wait.
from time import sleep

# Wait 5 Seconds.
sleep(5)

# Ask for first message and post it.
messageOne = input("Have something to say? ")
mc.postToChat(messageOne)

# Wait 3 seconds.
sleep(3)

# Ask for second message and post it.
messageTwo = input("Have something else to say? ")
mc.postToChat(messageTwo)
