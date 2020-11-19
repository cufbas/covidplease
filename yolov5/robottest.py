from pycreate2 import Create2
import time
import serial
import struct


def start(port):
    from pycreate2 import Create2

    # Create a Create2.
    bot = Create2(port)

    bot.start()

    # Start the Create 2
    #bot.start()

    # bot.wake()
    # bot.power()
    bot.full()

    # You are responsible for handling issues, no protection/safety in
    # this mode ... becareful
    # bot.full()
    #  time.sleep(1)
    # directly set the motor speeds ... move forward
    #  bot.drive_direct(100, 100)
    #  time.sleep(1)


    #  Stop the bot
    #  bot.drive_stop()


    print("turning on pump...")
    bot.pump_on()
    time.sleep(1)
    print("turning pump off")
    bot.pump_off()
    print("closing")
    bot.close()

if __name__ == '__main__':

    start('COM2')