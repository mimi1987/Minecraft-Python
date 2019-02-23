# Connect to minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Hardcode a message.
#message = "Hello Minecraft World!"
message = input("Have something to say? ") # Ask after player input.


# Display the message to the minecraft chat.
mc.postToChat(message)
