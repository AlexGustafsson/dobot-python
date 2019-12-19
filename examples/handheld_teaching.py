import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from lib.interface import Interface

bot = Interface('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

mode = bot.get_handheld_teaching_mode()
print('Mode:', mode)

state = bot.get_handheld_teaching_state()
print('State:', state)

trigger = bot.get_handheld_teaching_trigger()
print('Trigger:', trigger)

print('Activating handheld teaching mode')
bot.set_handheld_teaching_mode(0)
bot.set_handheld_teaching_state(True)
