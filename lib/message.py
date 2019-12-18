from lib.parsers import parsers


class Message:
    def __init__(self, header, length, id, rw, is_queued, params, direction='in'):
        self.header = header
        self.length = length
        self.id = id
        self.rw = rw
        self.is_queued = is_queued
        self.raw_params = []
        self.params = []

        if direction == 'in':
            self.raw_params = params
            self.params = self.parse_params('in')
        elif direction == 'out':
            self.params = params
            self.raw_params = self.parse_params('out')

    @staticmethod
    def calculate_checksum(payload):
        r = sum(payload) % 256
        # Calculate the two's complement
        check_byte = (256 - r) % 256
        return check_byte

    @staticmethod
    def verify_checksum(payload, checksum):
        a = sum(payload) % 256
        is_correct = True if (a + checksum) % 256 == 0 else False
        return is_correct

    @staticmethod
    def parse(message):
        bytes = list(message)

        header = bytes[0:2]
        length = bytes[2]
        id = bytes[3]
        control = bytes[4]
        rw = control & 1
        is_queued = control & 2
        params = bytes[5:-1]
        checksum = bytes[-1]

        verified = Message.verify_checksum([id] + [control] + params, checksum)

        if verified:
            return Message(header, length, id, rw, is_queued, params)
        else:
            return None

    @staticmethod
    def read(serial):
        header = serial.read(2)
        if header != b'\xaa\xaa':
            return None
        length = int.from_bytes(serial.read(1), 'little')
        payload = serial.read(length)
        checksum = serial.read(1)

        return Message.parse(header + bytes([length]) + payload + checksum)

    def parse_params(self, direction):
        parser = parsers[self.id]

        if direction == 'in':
            if parser is None:
                return None
            elif self.rw == 0 and self.is_queued == 0:
                return parser[0](self.raw_params)
            elif self.rw == 1 and self.is_queued == 0:
                return parser[0](self.raw_params)
            elif self.rw == 1 and self.is_queued == 1:
                return parser[2](self.raw_params)
            else:
                return []
        elif direction == 'out':
            if parser is None:
                return []
            elif direction == 'out' and self.rw == 1:
                return parser[3](self.params)
            else:
                return []

    def package(self):
        self.length = 2 + len(self.raw_params)
        control = int('000000' + str(int(self.is_queued)) + str(int(self.rw)), 2)
        self.checksum = Message.calculate_checksum([self.id] + [control] + self.raw_params)

        result = bytes(self.header + [self.length] + [self.id] + [control] + self.raw_params + [self.checksum])

        return result
