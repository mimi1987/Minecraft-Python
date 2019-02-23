from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Do you want blocks to be immutable? Y/N: ")
answer = answer.lower()

if answer == "y" or answer == "yes" or answer == "true":
    mc.setting("world_immutable", True)
    mc.postToChat("World is immutable")
else:
    mc.setting("world_immutable", False)
    mc.postToChat("World is mutable")

    
