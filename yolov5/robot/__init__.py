from pycreate2 import Create2
import argparse
import time
from random import randrange


class RobotControl:
    def __init__(self, port):
        self.bot = Create2(port)
        self.bot.start()  # Needed to make the robot operate
        self.bot.full()  # We're using safe so that we don't run over edges or some such
        self.sensor = self.bot.get_sensors()
        self.start = 0.0
        self.stop = 0.0

        self.turn_around()

    def update_sensor(self):
        # print('updating sensor')
        self.sensor = self.bot.get_sensors()
        #  print(self.sensor.light_bumper)
        end = (time.time() - self.start)
        print(end)
        print(self.sensor.light_bumper.center_right)
        # print(self.sensor.light_bumper_right)
        #  print(self.sensor.light_bumper.center_left)
        # print(end)

        if self.sensor.light_bumper.center_left > 50 or \
                self.sensor.light_bumper_center_right > 50 or \
                self.sensor.light_bumper_front_right > 50 or \
                self.sensor.light_bumper_front_left > 50:
            if 2 < end < 5:
                self.wall_detect()
            else:
                self.turn_around()

        # Turn left if you have meet something on the right
        elif self.sensor.light_bumper_right > 50 or self.sensor.light_bumper_front_right > 50:
            self.turn_right()

        # Turn right if you have meet something on the left
        elif self.sensor.light_bumper_left > 50 or self.sensor.light_bumper_front_left > 50:
            self.turn_left()

        elif end < randrange(start=5, stop=10):
            self.move_forward()

        else:
            self.turn_around()

    def wall_detect(self):
        print("Wall has been found!")
        self.move_forward()
        time.sleep(0.5)
        self.bot.pump_on()
        time.sleep(2)
        self.bot.pump_off()
        self.move_backwards()
        time.sleep(12)
        self.turn_around()
        time.sleep(15)
        #  self.bot.drive_direct(r_vel=-25, l_vel=-25)

    def turn_around(self):
        self.bot.drive_direct(l_vel=-25, r_vel=25)
        print("turning around")

    def turn_right(self):
        self.bot.drive_direct(l_vel=-10, r_vel=25)
        print("turning right")

    def turn_left(self):
        self.bot.drive_direct(l_vel=25, r_vel=-10)
        print("turning left")

    def move_forward(self):
        self.bot.drive_direct(r_vel=25, l_vel=25)
        print("moving forward")

    def move_backwards(self):
        self.bot.drive_direct(r_vel=-25, l_vel=-25)

    def main_movement(self, trackable):  # The main movement of the robot

        if not any(self.sensor.light_bumper):
            self.start = time.time()
            if trackable < 213:
                self.turn_right()
            elif 426 > trackable > 213:
                self.move_forward()
            elif trackable > 426:
                self.turn_left()
        else:
            self.update_sensor()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, default='COM2')
    opt = parser.parse_args()
