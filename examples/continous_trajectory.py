import sys
import os
sys.path.insert(0, os.path.abspath('.'))

import math

from lib.interface import Interface

bot = Interface('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

params = bot.get_continous_trajectory_params()
print('Params:', params)

[start_x, start_y, start_z, start_r] = bot.get_pose()[0:4]

bot.set_continous_trajectory_real_time_params(20, 100, 10)

# Draw about half an arch as a single path
bot.stop_queue()
steps = 12
scale = 75
for i in range(steps + 1):
    x = math.cos((math.pi / steps) * i)
    y = math.sin((math.pi / steps) * i)

    # Absolute movement
    bot.set_continous_trajectory_command(1, start_x, start_y + y * scale, start_z + x * scale, start_r)

bot.start_queue()
