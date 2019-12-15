import serial

from message import Message


class Dobot:
    def __init__(self, port):
        self.serial = serial.Serial(
            port=port,
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def connected(self):
        return self.serial.isOpen()

    def get_device_serial_number(self):
        request = Message([0xAA, 0xAA], 0x2, 0, 0, 0, [])
        self.serial.write(request.package())
        response = Message.read(self.serial)
        return response.get_param_as_string()

    def set_device_serial_number(self, serial_number):
        request = Message([0xAA, 0xAA], 0x2, 0, 1, 0, list(serial_number.encode('ascii')) + [0x00])
        self.serial.write(request.package())
        Message.read(self.serial)

    def get_device_name(self):
        request = Message([0xAA, 0xAA], 0x2, 1, 0, 0, [])
        self.serial.write(request.package())
        response = Message.read(self.serial)
        return response.get_param_as_string()

    def set_device_name(self, device_name):
        request = Message([0xAA, 0xAA], 0x2, 1, 1, 0, list(device_name.encode('ascii')) + [0x00])
        self.serial.write(request.package())
        Message.read(self.serial)

    def get_device_version(self):
        request = Message([0xAA, 0xAA], 0x2, 2, 0, 0, [])
        self.serial.write(request.package())
        response = Message.read(self.serial)
        return response.params[0:3]
