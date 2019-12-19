import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from time import sleep

from lib.interface import Interface

bot = Interface('/dev/tty.SLAB_USBtoUART')

# Defaults
bot.set_jog_joint_params([20, 20, 20, 30], [100, 100, 100, 100])
bot.set_jog_coordinate_params([20, 20, 20, 30], [100, 100, 100, 100])
bot.set_jog_common_params(150, 150)

print('Bot status:', 'connected' if bot.connected() else 'not connected')

joint_params = bot.get_jog_joint_params()
print('Joint params:', joint_params)

coordinate_params = bot.get_jog_coordinate_params()
print('Coordinate params:', coordinate_params)

common_params = bot.get_jog_common_params()
print('Common params:', common_params)

print('Rotating left')
bot.set_jog_command(1, 1)
sleep(1)

print('Rotating right')
bot.set_jog_command(1, 2)
sleep(1)

print('Stopping')
bot.set_jog_command(1, 0)
sleep(1)

print('Increasing joint speed')
bot.set_jog_joint_params([50, 50, 50, 30], [500, 500, 500, 500])

print('Moving forward')
bot.set_jog_command(1, 3)
sleep(1)

print('Moving backward')
bot.set_jog_command(1, 4)
sleep(1)

print('Stopping')
bot.set_jog_command(1, 0)
sleep(1)

print('Decreasing joint speed')
bot.set_jog_joint_params([10, 10, 10, 30], [100, 100, 100, 100])
print('Increasing coordinate speed')
bot.set_jog_coordinate_params([50, 50, 50, 30], [500, 500, 500, 500])

print('Moving down')
bot.set_jog_command(1, 5)
sleep(1)

print('Decreasing coordinate speed')
bot.set_jog_coordinate_params([10, 10, 10, 30], [100, 100, 100, 100])
print('Increasing general speed')
bot.set_jog_common_params(50, 50)

print('Moving up')
bot.set_jog_command(1, 6)
sleep(1)

print('Stopping')
bot.set_jog_command(1, 0)
sleep(1)
