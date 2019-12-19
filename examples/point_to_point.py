import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from time import sleep

from lib.interface import Interface

bot = Interface('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

joint_params = bot.get_point_to_point_joint_params()
print('Joint params:', joint_params)

jump_params = bot.get_point_to_point_jump_params()
print('Jump params:', jump_params)

jump2_params = bot.get_point_to_point_jump2_params()
print('Jump2 params:', jump2_params)

common_params = bot.get_point_to_point_common_params()
print('Common params:', common_params)

coordinate_params = bot.get_point_to_point_coordinate_params()
print('Coordinate params:', coordinate_params)

# Does nothing?
bot.set_point_to_point_command(0, 10, 10, 10, 10)
sleep(1)

# Does nothing?
bot.set_point_to_point_command(1, 30, 30, 30, 30)
sleep(1)

# One axis at a time
bot.set_point_to_point_command(3, 10, 10, 10, 10)
sleep(1)

# One axis at a time
bot.set_point_to_point_command(3, 30, 30, 30, 30)
sleep(1)

# Shortest path
bot.set_point_to_point_command(4, 10, 10, 10, 10)
sleep(1)

# Shortest path
bot.set_point_to_point_command(5, 30, 30, 30, 30)
sleep(1)

# Shortest path
bot.set_point_to_point_command(6, 10, 10, 10, 10)
sleep(1)

# Shortest path
bot.set_point_to_point_command(7, 30, 30, 30, 30)
sleep(1)

bot.set_point_to_point_command(8, 10, 10, 10, 10)
sleep(1)

# Does nothing?
bot.set_point_to_point_po_command(0, 30, 30, 30, 30)
