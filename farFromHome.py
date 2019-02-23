# Connect to Minecraft.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Is needed for sqrt.
import math

# My house.
homeX = 10
homeZ = 10

# My current position.
pos = mc.player.getTilePos()
x = pos.x
z = pos.z

# Use Pythagorean theorem.
distance = math.sqrt((homeX - x) ** 2 + (homeZ - z) ** 2)

# Ask the question distance is greater or equal to 40.
distance = distance >= 40

# Formulate a message.
message = "My house is nearby: " + str(distance)

# Post to Minecraft chat.
mc.postToChat(message)
