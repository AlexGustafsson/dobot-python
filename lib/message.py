class Message:
    def __init__(self, header, length, id, rw, is_queued, params):
        self.header = header
        self.length = length
        self.id = id
        self.rw = rw
        self.is_queued = is_queued
        self.params = params

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

    def package(self):
        self.length = 2 + len(self.params)
        control = int('000000' + str(self.is_queued) + str(self.rw), 2)
        self.checksum = Message.calculate_checksum([self.id] + [control] + self.params)

        result = bytes(self.header + [self.length] + [self.id] + [control] + self.params + [self.checksum])

        return result

    def get_param_as_string(self):
        return ''.join([chr(x) for x in self.params])
