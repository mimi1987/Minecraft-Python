# Connect to Minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Make the programm wait.
from time import sleep

# Wait for 5 seconds.
#sleep(5)

# Ask for the username.
username = input("Choose a name: ")

# Post a message with username.
message = input("Have something to say? ")
mc.postToChat(username + ": " + message)
