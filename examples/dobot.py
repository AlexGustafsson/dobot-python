import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from lib.dobot import Dobot

bot = Dobot('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

pose = bot.get_pose()
print('Pose:', pose)

print('Moving to absolute coordinate')
bot.move_to(20, 20, 20, 0.5)
# print('Moving to relative coordinate')
# bot.move_to_relative(15, 15, 15, 0.5)
# print('Moving back from relative coordinate')
# bot.move_to_relative(-15, -15, -15, -0.5)
#
# print('Sliding to absolute coordinate')
# bot.slide_to(40, 40, 40, 0.5)
# print('Sliding to relative coordinate')
# bot.slide_to_relative(15, 15, 15, 0.5)
# print('Sliding back from relative coordinate')
# bot.slide_to_relative(-15, -15, -15, -0.5)

print('Following a path')
bot.follow_path_relative([
    [5, 5, 5],
    [10, 0, 0],
    [0, 5, 0],
    [0, 0, 5]
])
