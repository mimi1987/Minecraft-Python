from mcpi.minecraft import Minecraft
mc = Minecraft.create()

username = input("Type a username: ")

while True:
    message = input(username + ": ")
    mc.postToChat(username + ": " + message)
