import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from time import sleep

from lib.interface import Interface

bot = Interface('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

device_name = bot.get_device_name()
print('Name:', device_name)

bot.set_device_name('dobot-python')
device_name = bot.get_device_name()
print('New name:', device_name)

device_id = bot.get_device_id()
print('ID:', device_id)

device_serial_number = bot.get_device_serial_number()
print('Serial number:', device_serial_number)

[device_version_major, device_version_minor, device_version_revision] = bot.get_device_version()
print('Version: {}.{}.{}'.format(device_version_major, device_version_minor, device_version_revision))

device_time = bot.get_device_time()
print('Time: {}ms'.format(device_time))

# Reset name
bot.set_device_name(device_name)
