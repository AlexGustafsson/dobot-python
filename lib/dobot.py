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

    def home(self):
        return self.interface.set_homing_command(0)

    # Move to the absolute coordinate, one axis at a time
    def move_to(self, x, y, z, r):
        return self.interface.set_point_to_point_command(3, x, y, z, r)

    # Slide to the absolute coordinate, shortest possible path
    def slide_to(self, x, y, z, r):
        # Moves in Manhattan coordinates
        return self.interface.set_point_to_point_command(4, x, y, z, r)

    # Move to the absolute coordinate, one axis at a time
    def move_to_relative(self, x, y, z, r):
        return self.interface.set_point_to_point_command(7, x, y, z, r)

    # Slide to the relative coordinate, one axis at a time
    def slide_to_relative(self, x, y, z, r):
        return self.interface.set_point_to_point_command(6, x, y, z, r)
