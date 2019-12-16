# Dobot Python
### A cross-platform low-level interface to the Dobot Magician robotic arm written in Python 3
***

### Setting up

##### Quickstart

```Bash
# Clone the repository
git clone https://github.com/AlexGustafsson/dobot-python
# Enter the directory
cd dobot-python
# Run an example program
python3 lib/test.py
```

```python
bot = Dobot('/dev/tty.usbserial-0001')

if bot.connected():
    print('Connected')
else:
    print('Not connected')

device_name = bot.get_device_name()
print('Hello, my name is {}'.format(device_name))

pose = bot.get_pose()
print('I am currently in the following pose:', pose)

print('I can move slow')
bot.set_joint_parameters(100, 50)
bot.move_to(100, 50, 20, 0)
bot.wait()

print('And I can move fast')
bot.set_joint_parameters(2000, 500)
bot.move_to_relative(20, 0, 0, 0)
bot.wait()
bot.move_to_relative(-20, 0, 0, 0)
bot.wait()

print('I even have a laser!')
bot.enable_laser()
```

### Motivation

The Dobot Magician seems like a fantastic robot arm. But my experience regarding its software and how to get it to work, or even access it, on different platforms have been one of the worst experiences I've had with a product.

Their Python SDK seems to be built around wrappers of various DLLs or dynamically linked libraries which lack any source. It can therefore not be considered especially open source or cross-platform.

The download server has been terrible, dropping downloads a few seconds in or reducing download speeds to a few KB/s. To make matters worse, their web site was hacked and redirected to a phishing website at the time of writing.

Once I was able to access their Magician Studio for macOS - it was all in Chinese without any real option to change language. I have been unable to try the Windows version due to the aforementioned issues with their website.

I was, however, able to access an API reference for their serial communication protocol which was well written and concise - so I decided to implement the protocol myself.

Previous art is https://github.com/luismesas/pydobot which implements a small subset of the protocol.

### Documentation

This library is currently actively being developed. It targets the Dobot Magician Communication Protocol v1.1.5 which is the latest version.

As often as possible, the names for functions, parameters etc. follow those documented in the communication protocol. There are convenience methods, such as `enable_laser` which is an alias to `set_laser_state`.

For now, refer to the source code as well as the example programs.

### Contributing

Any contribution is welcome. If you're not able to code it yourself, perhaps someone else is - so post an issue if there's anything on your mind.

###### Development

Clone the repository:
```
git clone https://github.com/AlexGustafsson/dobot-python && cd dobot-python
```

### Disclaimer

_Although the project is very capable, it is not built with production in mind. Therefore there might be complications when trying to use the bot for large-scale projects meant for the public. The library was created to easily use the Dobot Magician and as such it might not promote best practices nor be performant._
