import parsers


class Message:
    def __init__(self, header, length, id, rw, is_queued, params, direction='in'):
        self.header = header
        self.length = length
        self.id = id
        self.rw = rw
        self.is_queued = is_queued
        if direction == 'in':
            self.raw_params = params
            self.params = Message.parse_params(params, 'in')
        elif direction == 'out':
            self.params = params
            self.raw_params = Message.parse_params(params, 'out')

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
    def parse_params(message, direction):
        parser = parsers[message.id]

        if direction == 'in':
            if parser is None:
                return None
            elif message.rw == 0 and message.is_queued == 0:
                return parser[0](message.raw_params)
            elif message.rw == 1 and message.is_queued == 0:
                return parser[1](message.raw_params)
            elif message.rw == 1 and message.is_queued == 1:
                return parser[2](message.raw_params)
        elif direction == 'out':
            if parser is None:
                return []
            elif direction == 'out' and message.rw == 1:
                return parser[3](message.params)

    @staticmethod
    def read(serial):
        header = serial.read(2)
        if header != b'\xaa\xaa':
            return None

        length = int.from_bytes(serial.read(1), 'little')
        payload = serial.read(length)
        checksum = serial.read(1)

        return Message.parse(header + bytes([length]) + payload + checksum)

    def package(self):
        self.length = 2 + len(self.params)
        control = int('000000' + str(self.is_queued) + str(self.rw), 2)
        self.checksum = Message.calculate_checksum([self.id] + [control] + self.params)

        result = bytes(self.header + [self.length] + [self.id] + [control] + self.params + [self.checksum])

        return result
