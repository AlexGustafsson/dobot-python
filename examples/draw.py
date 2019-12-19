import sys
import os
sys.path.insert(0, os.path.abspath('.'))

import math

from lib.dobot import Dobot
bot = Dobot('/dev/tty.SLAB_USBtoUART')

print('Homing')
#bot.home()

print('Unlock the arm and place it on the middle of the paper')
input("Press enter to continue...")

center = bot.get_pose()
print('Center:', center)

bot.move_to_relative(0, 0, 10, 0)
print('Ready to draw')

bot.move_to_relative(0, 0, -10, 0)

bot.interface.set_continous_trajectory_params(200, 200, 200)

# Draw circle
path = []
steps = 24
scale = 50
for i in range(steps + 2):
    x = math.cos(((math.pi * 2) / steps) * i)
    y = math.sin(((math.pi * 2) / steps) * i)

    path.append([center[0] + x * scale, center[1] + y * scale, center[2]])
bot.follow_path(path)

# Move up and then back to the start
bot.move_to_relative(0, 0, 10, 0)
bot.slide_to(center[4], center[5], center[6], center[7])

# Draw circle
