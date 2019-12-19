import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from lib.interface import Interface

bot = Interface('/dev/tty.SLAB_USBtoUART')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

status = bot.get_wifi_status()
print('Status:', status)

if not status:
    print('Wifi not enabled, no more information to give')
    quit(0)

ssid = bot.get_wifi_ssid()
print('SSID:', ssid)

password = bot.get_wifi_password()
print('Password:', password)

address = bot.get_wifi_address()
print('Address:', address)

netmask = bot.get_wifi_netmask()
print('Netmask:', netmask)

gateway = bot.get_wifi_gateway()
print('Gateway:', gateway)

dns = bot.get_wifi_dns()
print('DNS:', dns)

connected = bot.get_wifi_connect_status()
print('Connected:', connected)
