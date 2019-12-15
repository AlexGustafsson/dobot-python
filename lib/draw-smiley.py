from time import sleep
import math

from dobot import Dobot

bot = Dobot('/dev/tty.usbserial-0001')

# Reset
bot.stop_queue()
bot.clear_queue()
bot.disable_laser()
bot.start_queue()

bot.home()
bot.wait()

start_pose = bot.get_pose()
print(start_pose)

# Be fast
bot.set_joint_parameters(500, 50)

scale = 20

# Move down
bot.move_to_relative(0, 0, -118, 0)
bot.wait()

# Go slow
bot.set_joint_parameters(2000, 100)

# Draw smile
bot.set_continous_joint_parameters(10, 10, 10)
bot.stop_queue()
bot.enable_laser()
steps = 24
draw_pos = bot.get_pose()
bot.stop_queue()
for i in range(steps + 1):
    x = math.cos(((0.5 * math.pi) / steps) * i)
    y = math.sin(((0.5 * math.pi) / steps) * i)

    bot.move_to_continous(draw_pos[0] + y * scale, draw_pos[1] + x * scale, draw_pos[2])
bot.disable_laser()
bot.start_queue()
bot.wait()
sleep(0.1)

# Be fast
bot.set_joint_parameters(500, 50)
# Move back up
bot.move_to(start_pose[0], start_pose[1], start_pose[2], start_pose[3])
