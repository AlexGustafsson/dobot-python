from dobot import Dobot

bot = Dobot('/dev/tty.usbserial-0001')

if bot.connected():
    print('Connected')
else:
    print('Not connected')

device_name = bot.get_device_name()
serial_number = bot.get_device_serial_number()
print(device_name, serial_number)
bot.set_device_name('Hello')
device_name = bot.get_device_name()
print(device_name, serial_number)
[major, minor, revision] = bot.get_device_version()
print(major, minor, revision)
