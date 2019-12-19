import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from lib.dobot import Dobot

bot = Dobot('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

pose = bot.get_pose()
print('Pose:', pose)

bot.move_to(20, 20, 20, 0.5)
bot.move_to_relative(15, 15, 15, 0.5)
bot.move_to_relative(-15, -15, -15, -0.5)

bot.slide_to(40, 40, 40, 0.5)
bot.slide_to_relative(15, 15, 15, 0.5)
bot.slide_to_relative(-15, -15, -15, -0.5)
