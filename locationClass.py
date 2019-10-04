from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Location(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


village = Location(-2175, 71, 790)

mc.player.setTilePos(village.x, village.y, village.z)
