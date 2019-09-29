from mcpi.minecraft import Minecraft
mc = Minecraft.create()

""" Script test if a diamond block is 50 blocks beneath my feets. """

diamondBlock = 56

while True:
    pos = mc.player.getTilePos()  # Get players position
    x, y, z = pos.x, pos.y, pos.z  # Initialize the coordinates (x,y,z)
    depths = range(50)  # Depth to test for diamond block

    # Test for diamond block
    for depth in depths:
        block = mc.getBlock(x, y - depth, z)  # Current block respectively to depth
        if block == diamondBlock:
            message = "Found a diamond block " + str(depth) + " blocks beneath you!"
            mc.postToChat(message)
            break  # Exit the for loop
    else:
        message = "No diamond block found!"
        mc.postToChat(message)
        
    

    
