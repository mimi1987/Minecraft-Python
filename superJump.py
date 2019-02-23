# Mit Minecraft verbinden.
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Spielers aktuelle Position.
position = mc.player.getTilePos()

# Koordinaten festlegen.
x = position.x
y = position.y
z = position.z

# Super Sprung.
y = y + 10
mc.player.setTilePos(x, y, z)


