from pycreate2 import Create2
import time
import serial
import struct

class SerialCommandInterface(object):
    """
    This class handles sending commands to the Create2. Writes will take in tuples
    and format the data to transfer to the Create.
    """

    def __init__(self):
        """
        Constructor.

        Creates the serial port, but doesn't open it yet. Call open(port) to open
        it.
        """
        self.ser = serial.Serial()

    def __del__(self):
        """
        Destructor.

        Closes the serial port
        """
        self.close()

    def open(self, port, baud=115200, timeout=2):
        """
        Opens a serial port to the create.

        port: the serial port to open, ie, '/dev/ttyUSB0'
        buad: default is 115200, but can be changed to a lower rate via the create api
        """
        self.ser.port = port
        self.ser.baudrate = baud
        self.ser.timeout = timeout
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.parity = serial.PARITY_NONE
        self.ser.setRTS(0)
        # print self.ser.name
        if self.ser.is_open:
            self.ser.close()
        self.ser.open()
        if self.ser.is_open:
            # print("Create opened serial: {}".format(self.ser))
            print('-'*40)
            print(' Create opened serial connection')
            print('   port: {}'.format(self.ser.port))
            print('   datarate: {} bps'.format(self.ser.baudrate))
            print('-'*40)
        else:
            raise Exception('Failed to open {} at {}'.format(port, baud))

    def write(self, opcode, data=None):
        """
        Writes a command to the create. There needs to be an opcode and optionally
        data. Not all commands have data associated with it.

        opcode: see creaet api
        data: a tuple with data associated with a given opcode (see api)
        """
        msg = (opcode,)

        # Sometimes opcodes don't need data. Since we can't add
        # a None type to a tuple, we have to make this check.
        if data:
            msg += data
        print(">> write:", msg)
        self.ser.write(struct.pack('B' * len(msg), *msg))
    def close(self):
        """
        Closes the serial connection.
        """
        if self.ser.is_open:
            print('Closing port {} @ {}'.format(self.ser.port, self.ser.baudrate))
            self.ser.close()


def start(port):
    from pycreate2 import Create2

    # Create a Create2.
    bot = Create2(port)

    bot.start()

    # Start the Create 2
    #bot.start()

    # bot.wake()
    # bot.power()
    bot.safe()

    # You are responsible for handling issues, no protection/safety in
    # this mode ... becareful
    # bot.full()
    #  time.sleep(1)
    # directly set the motor speeds ... move forward
    #  bot.drive_direct(100, 100)
    #  time.sleep(1)


    #  Stop the bot
    #  bot.drive_stop()

    bot.get_sensors()


if __name__ == '__main__':

    start('COM2')