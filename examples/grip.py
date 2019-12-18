import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from time import sleep

from lib.dobot import Dobot

bot = Dobot('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

status = bot.get_end_effector_gripper()
print('Status:', status)

bot.set_end_effector_gripper(True, False)
sleep(2)

bot.set_end_effector_gripper(True, True)
sleep(2)

bot.set_end_effector_gripper(True, False)
sleep(2)

bot.set_end_effector_gripper(False, False)
