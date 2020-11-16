from pycreate2 import Create2
import argparse
import time


class RobotControl:
    def __init__(self, port):
        self.bot = Create2(port)
        self.bot.start()  # Needed to make the robot operate
        self.bot.full()  # We're using safe so that we don't run over edges or some such

    def turn_right(self):
        #  self.bot.drive_direct(l_vel=10, r_vel=200)
        print("turning right")

    def turn_left(self):
        #  self.bot.drive_direct(l_vel=200, r_vel=10)
        print("turning left")

    def move_forward(self):
        #  self.bot.drive_direct(r_vel=50, l_vel=50)
        print("moving forward")

    def main_movement(self, trackable):  # The main movement of the robot

        # self.sensor = self.bot.get_sensors() Sensors currently don't work

        self.bot.stop()

        if trackable < 213:
            self.turn_left()
        elif 426 > trackable > 213:
            self.move_forward()
        elif trackable > 426:
            self.turn_right()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, default='COM2')
    opt = parser.parse_args()

    RobotControl(opt.port).main_movement()
