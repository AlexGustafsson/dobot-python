from dobot import Dobot

bot = Dobot('/dev/tty.usbserial-0001')

if bot.connected():
    print('Connected')
else:
    print('Not connected')

# Device info
device_name = bot.get_device_name()
print('Name: {}'.format(device_name))

device_id = bot.get_device_id()
print('ID: {}'.format(device_id))

device_serial_number = bot.get_device_serial_number()
print('Serial number: {}'.format(device_serial_number))

[device_version_major, device_version_minor, device_version_revision] = bot.get_device_version()
print('Version: {}.{}.{}'.format(device_version_major, device_version_minor, device_version_revision))

device_time = bot.get_device_time()
print('Time: {}'.format(device_time))

# Real-time pose
pose = bot.get_pose()
print('Pose:', pose)

bot.reset_pose(True, 0.5, 0.5)

# Alarms
alarms_state = bot.get_alarms_state()
print('Alarms:', alarms_state)

# Homing
homing_parameters = bot.get_homing_paramaters()
print('Homing parameters:', homing_parameters)

bot.set_homing_command(0)
print('Homing')

auto_leveling = bot.get_auto_leveling()
print('Auto leveling:', auto_leveling)
