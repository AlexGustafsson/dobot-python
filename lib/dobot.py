from time import sleep

from lib.interface import Interface


class Dobot:
    def __init__(self, port):
        self.interface = Interface(port)

        self.interface.stop_queue(True)
        self.interface.clear_queue()
        self.interface.start_queue()

        self.interface.set_point_to_point_jump_params(10, 10)
        self.interface.set_point_to_point_joint_params([50, 50, 50, 50], [50, 50, 50, 50])
        self.interface.set_point_to_point_coordinate_params(50, 50, 50, 50)

        # velocity and acceleration ratio
        self.interface.set_point_to_point_common_params(50, 50)
        self.interface.set_point_to_point_jump2_params(5, 5, 5)

        self.interface.set_jog_joint_params([50, 50, 50, 50], [50, 50, 50, 50])
        self.interface.set_jog_coordinate_params([50, 50, 50, 50], [50, 50, 50, 50])
        self.interface.set_jog_common_params(50, 50)

        self.interface.set_continous_trajectory_params(50, 50, 50)

    def connected(self):
        return self.interface.connected()

    def get_pose(self):
        return self.interface.get_pose()

    def printq(self):
        pose = self.get_pose()
        print('q:   ', ' '.join([f'{q:8.1f}' for q in pose[4:]]))

    def printx(self):
        pose = self.get_pose()
        print('x:   ', ' '.join([f'{q:8.1f}' for q in pose[:4]]))


    alarm_dict = {
        0x00: 'reset occurred',
        0x01: 'undefined instruction',
        0x02: 'file system error',
        0x03: 'communications error between MCU and FPGA',
        0x04: 'angle sensor error',

        0x10: 'plan: pose is abnormal',
        0x11: 'plan: pose is out of workspace',
        0x12: 'plan: joint limit',
        0x13: 'plan: repetitive points',
        0x14: 'plan: arc input parameter',
        0x15: 'plan: jump parameter',

        0x20: 'motion: kinematic singularity',
        0x21: 'motion: out of workspace',
        0x22: 'motion: inverse limit',

        0x30: 'axis 1 overspeed',
        0x31: 'axis 2 overspeed',
        0x32: 'axis 3 overspeed',
        0x33: 'axis 4 overspeed',

        0x40: 'axis 1 positive limit',
        0x41: 'axis 1 negative limit',
        0x42: 'axis 2 positive limit',
        0x43: 'axis 2 negative limit',
        0x44: 'axis 3 positive limit',
        0x45: 'axis 3 negative limit',
        0x46: 'axis 4 positive limit',
        0x47: 'axis 4 negative limit',

        0x50: 'axis 1 lost steps',
        0x51: 'axis 2 lost steps',
        0x52: 'axis 3 lost steps',
        0x53: 'axis 4 lost steps',
    }

    def print_alarms(self, a):
        alarms = []
        for i, x in enumerate(a):
            for j in range(8):
                if x & (1<<j) > 0:
                    alarms.append(8*i + j)
        for alarm in alarms:
            print('ALARM:', self.alarm_dict[alarm])

    def home(self, wait=True):
        self.interface.set_homing_command(0)
        if wait:
            self.wait()

    # Move to the absolute coordinate, one axis at a time
    def move_to(self, x, y, z, r, wait=True):
        self.interface.set_point_to_point_command(3, x, y, z, r)
        if wait:
            self.wait()

    # Slide to the absolute coordinate, shortest possible path
    def slide_to(self, x, y, z, r, wait=True):
        self.interface.set_point_to_point_command(4, x, y, z, r)
        if wait:
            self.wait()

    # Move to the absolute coordinate, one axis at a time
    def move_to_relative(self, x, y, z, r, wait=True):
        self.interface.set_point_to_point_command(7, x, y, z, r)
        if wait:
            self.wait()

    # Slide to the relative coordinate, one axis at a time
    def slide_to_relative(self, x, y, z, r, wait=True):
        self.interface.set_point_to_point_command(6, x, y, z, r)
        if wait:
            self.wait()

    # Wait until the instruction finishes
    def wait(self, queue_index=None):
        # If there are no more instructions in the queue, it will end up
        # always returning the last instruction - even if it has finished.
        # Use a zero wait as a non-operation to bypass this limitation
        self.interface.wait(0)

        if queue_index is None:
            queue_index = self.interface.get_current_queue_index()
        while True:
            if self.interface.get_current_queue_index() > queue_index:
                break

            sleep(0.5)

    # Move according to the given path
    def follow_path(self, path, wait=True):
        self.interface.stop_queue()
        queue_index = None
        for point in path:
            queue_index = self.interface.set_continous_trajectory_command(1, point[0], point[1], point[2], 50)
        self.interface.start_queue()
        if wait:
            self.wait(queue_index)

    # Move according to the given path
    def follow_path_relative(self, path, wait=True):
        self.interface.stop_queue()
        queue_index = None
        for point in path:
            queue_index = self.interface.set_continous_trajectory_command(0,  point[0], point[1], point[2], 50)
        self.interface.start_queue()
        if wait:
            self.wait(queue_index)
