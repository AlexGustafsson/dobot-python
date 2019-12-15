from time import sleep
import math

from dobot import Dobot

bot = Dobot('/dev/tty.usbserial-0001')

# Reset
bot.stop_queue()
bot.clear_queue()
bot.start_queue()

bot.home()
bot.wait()

start_pose = bot.get_pose()
print(start_pose)

# Be fast
bot.set_joint_parameters(500, 50)

# Move down
bot.move_to_relative(0, 0, -120, 0)
bot.wait()

# Go slow
bot.set_joint_parameters(5000, 1)

# Draw smile
steps = 60
scale = 20
draw_pos = bot.get_pose()
for i in range(steps):
    x = math.cos(((2 * math.pi) / steps) * i)
    y = math.sin(((2 * math.pi) / steps) * i)
    print(x, y)

    bot.move_to(draw_pos[0] + y * scale, draw_pos[1] + x * scale, draw_pos[2], draw_pos[3])
    bot.wait()

# Be fast
bot.set_joint_parameters(500, 50)
# Move back up
bot.move_to(start_pose[0], start_pose[1], start_pose[2], start_pose[3])
