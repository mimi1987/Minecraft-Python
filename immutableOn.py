# Connect to minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Change the settings.
mc.setting("world_immutable", True)
