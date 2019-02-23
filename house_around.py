from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()

answer = input("Create a house around me? Y/N: ")
answer = answer.lower()

if answer == "y":
    mc.setBlocks(pos.x-4, pos.y, pos.z-4, pos.x+4, pos.y+4, pos.z+4, 4)
    mc.setBlocks(pos.x-3, pos.y, pos.z-3, pos.x+3, pos.y+3, pos.z+3, 0)
    mc.postToChat("My house!")
