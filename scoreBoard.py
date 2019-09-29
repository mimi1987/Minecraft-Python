from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

""" A minigame within Minecraft that counts the blockhits with the
    right Mouseclick for 60 seconds and saves the player name and
    block hits in a dictionary. """

players = {}  # Stores the players names and scores
naem = ""  # Stores players name

while True:
    mc.postToChat("Block Hit Game! What's your name?")
    name = str(input("What's your name? ('exit' to quit) "))
    if name.lower() == "exit":
        break

    players[name] = 0  # Adds the player to the scoreboard

    mc.postToChat("Go!")

    time.sleep(60)

    blockHits = len(mc.events.pollBlockHits())  # Get the sum of blocks hit

    # Add the score to the player
    if name in players:
        if players[name] < blockHits:
            players[name] = blockHits
    else:
        players[name] = blockHits

    # Display the score of a player
    for key in players:
        message = key.capitalize() + " => " + str(players[key])
        mc.postToChat(message)

