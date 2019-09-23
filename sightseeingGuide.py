from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Add locations to the dictionary
places = {
        'mountain_view': (765, 78, -833),
        'flower_lake': (712, 70, -757),
        'lava_pool': (673, 64, -836),
        'cave_roof': (606, 78, -708),
        'deep_canyon': (648, 31, -707),
        'village': (840, 72, -684)
    }

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x, y, z = location
        mc.player.setTilePos(x, y, z)
