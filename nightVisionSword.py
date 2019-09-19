"""
Posts a message in the game chat if a diamond block is hit with the right click.
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

blocks = []

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        hitX, hitY, hitZ = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(hitX, hitY, hitZ)
        blocks.append(block)

    if 56 in blocks:
        mc.postToChat("Found a diamond block.")
        break

    time.sleep(0.2)

    
