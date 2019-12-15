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
pose = bot.get_pose()
print(pose)
# bot.home()
bot.move_to(pose[0] - 150, pose[1], pose[2], pose[3])
bot.move_to(pose[0], pose[1], pose[2], pose[3])
bot.move_to_relative(0, 20, 0, 0)
bot.move_to_relative(0, -20, 0, 0)
