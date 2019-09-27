from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {}

while True:
    # Get the players's name
    name = input("What is your name? ")

    # Break the loop if the name is exit
    if name == "exit":
        break
    mc.postToChat("Go!")

    # Wait 60 seconds
    time.sleep(60)

    # Get the list of block hits
    blockHits = mc.events.pollBlockHits()

    # Display the length of the block hits list to chat
    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockHitsLength))

    # Add the player to the scoreboard
    scoreboard[name] = blockHitsLength

    # Display the scoreboard
    print(scoreboard)

