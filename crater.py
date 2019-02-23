from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()

answer = input("Create a crater? Y/N: ")
answer = answer.lower()

if answer == "y":
    mc.setBlocks(pos.x+1, pos.y+1, pos.z+1, pos.x-1, pos.y-1, pos.z-1, 0)
    mc.postToChat("Boom")
else:
    print("No crater!")

    
