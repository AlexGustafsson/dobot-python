import serial
import threading
from time import sleep

from message import Message


class Dobot:
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.lock = threading.Lock()

        self.serial = serial.Serial(
            port=port,
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )

    def send(self, message):
        self.lock.acquire()
        self.serial.write(message.package())
        self.lock.release()
        response = Message.read(self.serial)
        return response.params

    def connected(self):
        return self.serial.isOpen()

    def get_device_serial_number(self):
        request = Message([0xAA, 0xAA], 2, 0, 0, 0, [])
        return self.send(request)

    def set_device_serial_number(self, serial_number):
        request = Message([0xAA, 0xAA], 2, 0, 1, 0, [serial_number])
        return self.send(request)

    def get_device_name(self):
        request = Message([0xAA, 0xAA], 2, 1, 0, 0, [])
        return self.send(request)

    def set_device_name(self, device_name):
        request = Message([0xAA, 0xAA], 2, 1, 1, 0, [device_name])
        return self.send(request)

    def get_device_version(self):
        request = Message([0xAA, 0xAA], 2, 2, 0, 0, [])
        return self.send(request)

    def set_sliding_rail_status(self, enable, version):
        request = Message([0xAA, 0xAA], 2, 3, 1, 0, [])
        return self.send(request)

    def get_device_time(self):
        request = Message([0xAA, 0xAA], 2, 4, 0, 0, [])
        return self.send(request)

    def get_device_id(self):
        request = Message([0xAA, 0xAA], 2, 5, 0, 0, [])
        return self.send(request)

    def get_pose(self):
        request = Message([0xAA, 0xAA], 2, 10, 0, 0, [])
        return self.send(request)

    def reset_pose(self, manual, rear_arm_angle, front_arm_angle):
        request = Message([0xAA, 0xAA], 2, 11, 1, 0, [manual, rear_arm_angle, front_arm_angle])
        return self.send(request)

    def get_sliding_rail_pose(self):
        request = Message([0xAA, 0xAA], 2, 13, 0, 0, [])
        return self.send(request)

    def get_alarms_state(self):
        request = Message([0xAA, 0xAA], 2, 20, 0, 0, [])
        return self.send(request)

    def clear_alarms_state(self):
        request = Message([0xAA, 0xAA], 2, 21, 1, 0, [])
        return self.send(request)

    def get_homing_paramaters(self):
        request = Message([0xAA, 0xAA], 2, 30, 0, 0, [])
        return self.send(request)

    def set_homing_parameters(self, x, y, z, r, queue=True):
        request = Message([0xAA, 0xAA], 2, 30, 1, queue, [x, y, z, r])
        return self.send(request)

    def set_homing_command(self, command, queue=True):
        request = Message([0xAA, 0xAA], 2, 31, 1, queue, [command])
        return self.send(request)

    def get_auto_leveling(self, queue=True):
        request = Message([0xAA, 0xAA], 2, 32, 1, queue, [])
        return self.send(request)

    def set_auto_leveling(self, enable, accuracy, queue=True):
        request = Message([0xAA, 0xAA], 2, 32, 1, queue, [enable, accuracy])
        return self.send(request)

    def get_handheld_teaching_mode(self):
        request = Message([0xAA, 0xAA], 2, 40, 0, 0, [])
        return self.send(request)

    def set_handheld_teaching_mode(self, mode):
        request = Message([0xAA, 0xAA], 2, 40, 1, 0, [])
        return self.send(request)

    def get_handheld_teaching_state(self):
        request = Message([0xAA, 0xAA], 2, 41, 0, 0, [])
        return self.send(request)

    def set_handheld_teaching_state(self, enable):
        request = Message([0xAA, 0xAA], 2, 41, 1, 0, [enable])
        return self.send(request)

    def get_handheld_teaching_trigger(self):
        request = Message([0xAA, 0xAA], 2, 42, 0, 0, [])
        return self.send(request)

    def get_end_effector_params(self):
        request = Message([0xAA, 0xAA], 2, 60, 0, 0, [])
        return self.send(request)

    def set_end_effector_params(self, bias_x, bias_y, bias_z):
        request = Message([0xAA, 0xAA], 2, 60, 1, 0, [bias_x, bias_y, bias_z])
        return self.send(request)

    def get_end_effector_laser(self):
        request = Message([0xAA, 0xAA], 2, 61, 0, 0, [])
        return self.send(request)

    def set_end_effector_laser(self, enable_control, enable_laser, queue=True):
        request = Message([0xAA, 0xAA], 2, 61, 1, queue, [enable_control, enable_laser])
        return self.send(request)

    def get_end_effector_suction_cup(self):
        request = Message([0xAA, 0xAA], 2, 62, 0, 0, [])
        return self.send(request)

    def set_end_effector_suction_cup(self, enable_control, enable_suction, queue=True):
        request = Message([0xAA, 0xAA], 2, 62, 1, queue, [enable_control, enable_suction])
        return self.send(request)

    def get_end_effector_gripper(self):
        request = Message([0xAA, 0xAA], 2, 63, 0, 0, [])
        return self.send(request)

    def set_end_effector_gripper(self, enable_control, enable_grip, queue=True):
        request = Message([0xAA, 0xAA], 2, 63, 1, queue, [enable_control, enable_grip])
        return self.send(request)

    def get_jog_joint_params(self):
        request = Message([0xAA, 0xAA], 2, 70, 0, 0, [])
        return self.send(request)

    def set_jog_joint_params(self, velocity, acceleration, queue=True):
        request = Message([0xAA, 0xAA], 2, 70, 1, queue, velocity + acceleration)
        return self.send(request)

    def get_jog_coordinate_params(self):
        request = Message([0xAA, 0xAA], 2, 71, 0, 0, [])
        return self.send(request)

    def set_jog_coordinate_params(self, velocity, acceleration, queue=True):
        request = Message([0xAA, 0xAA], 2, 71, 1, queue, velocity + acceleration)
        return self.send(request)

    def get_jog_common_params(self):
        request = Message([0xAA, 0xAA], 2, 72, 0, 0, [])
        return self.send(request)

    def set_jog_common_params(self, velocity_ratio, acceleration_ratio, queue=True):
        request = Message([0xAA, 0xAA], 2, 73, 1, queue, [velocity_ratio, acceleration_ratio])
        return self.send(request)

    def set_jog_command(self, jog_type, command, queue=True):
        request = Message([0xAA, 0xAA], 2, 73, 1, queue, [jog_type, command])
        return self.send(request)

    def get_sliding_rail_jog_params(self):
        request = Message([0xAA, 0xAA], 2, 74, 0, 0, [])
        return self.send(request)

    def set_sliding_rail_jog_params(self, velocity, acceleration, queue=True):
        request = Message([0xAA, 0xAA], 2, 74, 1, queue, [velocity, acceleration])
        return self.send(request)

    def get_point_to_point_joint_params(self):
        request = Message([0xAA, 0xAA], 2, 80, 0, 0, [])
        return self.send(request)

    def set_point_to_point_joint_params(self, velocity, acceleration, queue=True):
        request = Message([0xAA, 0xAA], 2, 80, 1, queue, velocity + acceleration)
        return self.send(request)

    def get_point_to_point_coordinate_params(self):
        request = Message([0xAA, 0xAA], 2, 81, 0, 0, [])
        return self.send(request)

    def set_point_to_point_coordinate_params(self, coordinate_velocity, effector_velocity, coordinate_acceleration, effector_acceleration, queue=True):
        request = Message([0xAA, 0xAA], 2, 81, 1, queue, [coordinate_velocity, effector_velocity, coordinate_acceleration, effector_acceleration])
        return self.send(request)

    def get_point_to_point_jump_params(self):
        request = Message([0xAA, 0xAA], 2, 82, 0, 0, [])
        return self.send(request)

    def set_point_to_point_jump_params(self, jump_height, z_limit, queue=True):
        request = Message([0xAA, 0xAA], 2, 82, 1, queue, [jump_height, z_limit])
        return self.send(request)

    def get_point_to_point_common_params(self):
        request = Message([0xAA, 0xAA], 2, 83, 0, 0, [])
        return self.send(request)

    def set_point_to_point_common_params(self, velocity_ratio, acceleration_ratio, queue=True):
        request = Message([0xAA, 0xAA], 2, 84, 1, queue, [velocity_ratio, acceleration_ratio])
        return self.send(request)

    def set_point_to_point_command(self, mode, x, y, z, r, queue=True):
        request = Message([0xAA, 0xAA], 2, 84, 1, queue, [mode, x, y, z, r])
        return self.send(request)

    def get_point_to_point_sliding_rail_params(self):
        request = Message([0xAA, 0xAA], 2, 85, 0, 0, [])
        return self.send(request)

    def set_point_to_point_sliding_rail_params(self, velocity, acceleration, queue=True):
        request = Message([0xAA, 0xAA], 2, 85, 1, queue, [velocity, acceleration])
        return self.send(request)

    def set_point_to_point_sliding_rail_command(self, mode, x, y, z, r, l, queue=True):
        request = Message([0xAA, 0xAA], 2, 86, 1, queue, [mode, x, y, z, r, l])
        return self.send(request)

    def get_point_to_point_jump2_params(self):
        request = Message([0xAA, 0xAA], 2, 87, 0, 0, [])
        return self.send(request)

    def set_point_to_point_jump2_params(self, start_height, end_height, z_limit, queue=True):
        request = Message([0xAA, 0xAA], 2, 87, 1, queue, [start_height, end_height, z_limit])
        return self.send(request)

    def set_point_to_point_po_command(self, mode, x, y, z, r, queue=True):
        request = Message([0xAA, 0xAA], 2, 88, 1, queue, [mode, x, y, z, r])
        return self.send(request)

    def set_point_to_point_sliding_rail_po_command(self, ratio, address, level, queue=True):
        request = Message([0xAA, 0xAA], 2, 89, 1, queue, [ratio, address, level])
        return self.send(request)

    def get_continous_trajectory_params(self):
        request = Message([0xAA, 0xAA], 2, 90, 0, 0, [])
        return self.send(request)

    def set_continous_trajectory_params(self, max_planned_acceleration, max_junction_velocity, acceleration, queue=True):
        request = Message([0xAA, 0xAA], 2, 90, 1, queue, [max_planned_acceleration, max_junction_velocity, acceleration, 0])
        return self.send(request)

    def set_continous_trajectory_real_time_params(self, max_planned_acceleration, max_junction_velocity, period, queue=True):
        request = Message([0xAA, 0xAA], 2, 90, 1, queue, [max_planned_acceleration, max_junction_velocity, period, 1])
        return self.send(request)

    def set_continous_trajectory_command(self, mode, x, y, z, velocity, queue=True):
        request = Message([0xAA, 0xAA], 2, 91, 1, queue, [mode, x, y, z, velocity])
        return self.send(request)

    def set_continous_trajectory_laser_engraver_command(self, mode, x, y, z, power, queue=True):
        request = Message([0xAA, 0xAA], 2, 92, 1, queue, [mode, x, y, z, power])
        return self.send(request)

    def get_arc_params(self):
        request = Message([0xAA, 0xAA], 2, 100, 0, 0, [])
        return self.send(request)

    def set_arc_params(self, coordinate_velocity, effector_velocity, coordinate_acceleration, effector_acceleration, queue=True):
        request = Message([0xAA, 0xAA], 2, 100, 1, queue, [coordinate_velocity, effector_velocity, coordinate_acceleration, effector_acceleration])
        return self.send(request)

    def set_arc_command(self, starting_point, ending_point, queue=True):
        request = Message([0xAA, 0xAA], 2, 101, 1, queue, starting_point + ending_point)
        return self.send(request)

    # Named 'wait' in the protocol specification
    def sleep(self, starting_point, milliseconds, queue=True):
        request = Message([0xAA, 0xAA], 2, 110, 1, queue, [milliseconds])
        return self.send(request)

    # Named 'wait' in the protocol specification
    def set_trigger_command(self, address, mode, condition, threshold, queue=True):
        request = Message([0xAA, 0xAA], 2, 120, 1, queue, [address, mode, condition, threshold])
        return self.send(request)

    def get_io_multiplexing(self):
        request = Message([0xAA, 0xAA], 2, 130, 0, 0, [])
        return self.send(request)

    def set_io_multiplexing(self, address, multiplex, queue=True):
        request = Message([0xAA, 0xAA], 2, 130, 1, queue, [address, multiplex])
        return self.send(request)

    def get_io_do(self):
        request = Message([0xAA, 0xAA], 2, 131, 0, 0, [])
        return self.send(request)

    def set_io_do(self, address, level, queue=True):
        request = Message([0xAA, 0xAA], 2, 131, 1, queue, [address, level])
        return self.send(request)

    def get_io_pwm(self):
        request = Message([0xAA, 0xAA], 2, 132, 0, 0, [])
        return self.send(request)

    def set_io_pwm(self, address, frequency, duty_cycle, queue=True):
        request = Message([0xAA, 0xAA], 2, 132, 1, queue, [address, frequency, duty_cycle])
        return self.send(request)

    def get_io_di(self):
        request = Message([0xAA, 0xAA], 2, 133, 0, 0, [])
        return self.send(request)

    def get_io_adc(self):
        request = Message([0xAA, 0xAA], 2, 134, 0, 0, [])
        return self.send(request)

    def set_extended_motor_velocity(self, index, enable, speed, queue=True):
        request = Message([0xAA, 0xAA], 2, 135, 1, queue, [index, enable, speed])
        return self.send(request)

    def get_color_sensor(self, index):
        request = Message([0xAA, 0xAA], 2, 137, 0, 0, [])
        return self.send(request)

    def set_color_sensor(self, index, enable, port, version, queue=True):
        request = Message([0xAA, 0xAA], 2, 137, 1, queue, [enable, port, version])
        return self.send(request)

    def get_ir_switch(self, index):
        request = Message([0xAA, 0xAA], 2, 138, 0, 0, [])
        return self.send(request)

    def set_ir_switch(self, index, enable, port, version, queue=True):
        request = Message([0xAA, 0xAA], 2, 138, 1, queue, [enable, port, version])
        return self.send(request)

    def get_angle_sensor_static_error(self, index):
        request = Message([0xAA, 0xAA], 2, 140, 0, 0, [])
        return self.send(request)

    def set_angle_sensor_static_error(self, index, rear_arm_angle_error, front_arm_angle_error):
        request = Message([0xAA, 0xAA], 2, 140, 1, 0, [rear_arm_angle_error, front_arm_angle_error])
        return self.send(request)

    def get_wifi_status(self, index):
        request = Message([0xAA, 0xAA], 2, 150, 0, 0, [])
        return self.send(request)

    def set_wifi_status(self, index, enable):
        request = Message([0xAA, 0xAA], 2, 150, 1, 0, [enable])
        return self.send(request)

    def get_wifi_ssid(self, index):
        request = Message([0xAA, 0xAA], 2, 151, 0, 0, [])
        return self.send(request)

    def set_wifi_ssid(self, index, ssid):
        request = Message([0xAA, 0xAA], 2, 151, 1, 0, [ssid])
        return self.send(request)

    def get_wifi_password(self, index):
        request = Message([0xAA, 0xAA], 2, 152, 0, 0, [])
        return self.send(request)

    def set_wifi_password(self, index, ssid):
        request = Message([0xAA, 0xAA], 2, 152, 1, 0, [ssid])
        return self.send(request)

    def get_wifi_address(self, index):
        request = Message([0xAA, 0xAA], 2, 153, 0, 0, [])
        return self.send(request)

    # 192.168.1.1 = a.b.c.d
    def set_wifi_address(self, index, use_dhcp, a, b, c, d):
        request = Message([0xAA, 0xAA], 2, 153, 1, 0, [use_dhcp, a, b, c, d])
        return self.send(request)

    def get_wifi_netmask(self, index):
        request = Message([0xAA, 0xAA], 2, 154, 0, 0, [])
        return self.send(request)

    # 255.255.255.0 = a.b.c.d
    def set_wifi_netmask(self, index, a, b, c, d):
        request = Message([0xAA, 0xAA], 2, 154, 1, 0, [a, b, c, d])
        return self.send(request)

    def get_wifi_gateway(self, index):
        request = Message([0xAA, 0xAA], 2, 155, 0, 0, [])
        return self.send(request)

    # 192.168.1.1 = a.b.c.d
    def set_wifi_gateway(self, index, use_dhcp, a, b, c, d):
        request = Message([0xAA, 0xAA], 2, 155, 1, 0, [use_dhcp, a, b, c, d])
        return self.send(request)

    def get_wifi_dns(self, index):
        request = Message([0xAA, 0xAA], 2, 156, 0, 0, [])
        return self.send(request)

    # 192.168.1.1 = a.b.c.d
    def set_wifi_dns(self, index, use_dhcp, a, b, c, d):
        request = Message([0xAA, 0xAA], 2, 156, 1, 0, [use_dhcp, a, b, c, d])
        return self.send(request)

    def get_wifi_connect_status(self):
        request = Message([0xAA, 0xAA], 2, 157, 0, 0, [])
        return self.send(request)

    def set_lost_step_params(self, param):
        request = Message([0xAA, 0xAA], 2, 170, 1, 0, [param])
        return self.send(request)

    def set_lost_step_command(self):
        request = Message([0xAA, 0xAA], 2, 171, 1, 0, [])
        return self.send(request)

    def start_queue(self):
        request = Message([0xAA, 0xAA], 2, 240, 1, 0, [])
        return self.send(request)

    def stop_queue(self, force=False):
        request = Message([0xAA, 0xAA], 2, 242 if force else 241, 1, 0, [])
        return self.send(request)

    def start_queue_download(self, total_loop, line_per_loop):
        request = Message([0xAA, 0xAA], 2, 243, 1, 0, [total_loop, line_per_loop])
        return self.send(request)

    def stop_queue_download(self):
        request = Message([0xAA, 0xAA], 2, 244, 1, 0, [])
        return self.send(request)

    def clear_queue(self):
        request = Message([0xAA, 0xAA], 2, 245, 1, 0, [])
        return self.send(request)

    def get_current_queue_index(self):
        request = Message([0xAA, 0xAA], 2, 246, 1, 0, [])
        return self.send(request)
