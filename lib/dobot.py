import serial
import struct

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
        request = Message([0xAA, 0xAA], 2, 0, 0, 0, [])
        self.serial.write(request.package())
        response = Message.read(self.serial)
        return response.get_param_as_string()

    def set_device_serial_number(self, serial_number):
        request = Message([0xAA, 0xAA], 2, 0, 1, 0, list(serial_number.encode('ascii')) + [0x00])
        self.serial.write(request.package())
        Message.read(self.serial)

    def get_device_name(self):
        request = Message([0xAA, 0xAA], 2, 1, 0, 0, [])
        self.serial.write(request.package())
        response = Message.read(self.serial)
        return response.get_param_as_string()

    def set_device_name(self, device_name):
        request = Message([0xAA, 0xAA], 2, 1, 1, 0, list(device_name.encode('ascii')) + [0x00])
        self.serial.write(request.package())
        Message.read(self.serial)

    def get_device_version(self):
        request = Message([0xAA, 0xAA], 2, 2, 0, 0, [])
        self.serial.write(request.package())
        response = Message.read(self.serial)
        return response.params[0:3]

    def get_pose(self):
        request = Message([0xAA, 0xAA], 2, 10, 0, 0, [])
        self.serial.write(request.package())
        response = Message.read(self.serial)
        return struct.unpack('ffffffff', bytes(response.params))

    def home(self):
        request = Message([0xAA, 0xAA], 2, 31, 1, 0, [])
        self.serial.write(request.package())
        Message.read(self.serial)

    def move_to(self, x, y, z, r, wait=True, mode=2):
        is_queued = 1 if wait else 0
        request = Message([0xAA, 0xAA], 2, 84, 1, is_queued, [mode] + list(struct.pack('<ffff', x, y, z, r)))
        self.serial.write(request.package())
        response = Message.read(self.serial)
        if is_queued:
            queue_index = struct.unpack('L', bytes(response.params))
            return queue_index
        return None

    def move_to_relative(self, x, y, z, r, wait=True):
        return self.move_to(x, y, z, r, wait, 8)

    def get_joint_paramaters(self):
        request = Message([0xAA, 0xAA], 2, 83, 0, 0, [])
        self.serial.write(request.package())
        response = Message.read(self.serial)
        return struct.unpack('<ff', bytes(response.params))

    def set_joint_parameters(self, velocity_ratio, acceleration_ratio, wait=True):
        if acceleration_ratio <= 0:
            return None

        is_queued = 1 if wait else 0
        request = Message([0xAA, 0xAA], 2, 83, 1, is_queued, list(struct.pack('<ff', velocity_ratio, acceleration_ratio)))
        self.serial.write(request.package())
        response = Message.read(self.serial)
        if is_queued:
            queue_index = struct.unpack('L', bytes(response.params))
            return queue_index
        return None
