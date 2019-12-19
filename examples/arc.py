import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from time import sleep

from lib.interface import Interface

bot = Interface('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

params = bot.get_arc_params()
print('Params:', params)

# Default start position
bot.set_homing_command(0)
sleep(4)

[x, y, z, r] = bot.get_pose()[0:4]
bot.set_arc_command([x + 50, y, z, r], [x - 50, y + 50, z, r])
bot.set_arc_command([x + 50, y, z, r], [x - 50, y + 50, z, r])
