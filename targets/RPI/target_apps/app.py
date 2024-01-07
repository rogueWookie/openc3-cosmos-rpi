#!/usr/bin/python3
import serial
import time
from ctypes import *
from enum import Enum


class Cfg(Enum):
    """
    @about
    An enumeration of constants for this apps configuration

    @enums
    SYN_MRK_INFO - The sync marker expressed in BIG_ENDIAN
    SER_PRT_INFO - The serial port file descriptor in /dev
    SER_BUD_INFO - The baudrate of the serial port
    SER_TOT_READ - The read timeout on the serial port
    """
    SYN_MRK_INFO = 0xDEADBEEF
    SER_PRT_INFO = '/dev/ttyUSB0'
    SER_BUD_INFO = 115200
    SER_TOT_READ = 1


class PacketCounters(Structure):
    """
    @about
    A telemetry packet of telemetry items being counters

    @items
    sync_marker     - The sync marker that deliniates packets
    packet_length   - The length of the packed ctype structure
    packet_apid     - Application identifier for this packet
    x_counter       - Counter going up by one
    y_counter       - Counter going up by two
    """
    _pack_ = 1
    _fields_ = [
            ("sync_marker", c_uint),
            ("packet_length", c_uint),
            ("packet_apid", c_uint),
            ("x_counter", c_ubyte),
            ("y_counter", c_ubyte)]

    def __init__(self, x=0, y=0):
        self.sync_marker = Cfg.SYN_MRK_INFO.value
        self.packet_length = sizeof(self)
        self.packet_apid = 1
        self.x_counter = x
        self.y_counter = y

    def packet_increment(self):
        self.x_counter += 1
        self.y_counter += 2


class InterfaceSerial:
    """
    @about
    A interface class for serial port interfacing

    @params
    logging - turns on/off print statements to declutter console
    """
    def __init__(self, logging=False):
        self.ser = serial.Serial(
                Cfg.SER_PRT_INFO.value, 
                Cfg.SER_BUD_INFO.value, 
                timeout=Cfg.SER_TOT_READ.value)
        self.logging = logging
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def interface_write(self, pkt):
        length = len(bytearray(pkt))
        buffer = bytearray(pkt)
        if self.ser.write(buffer) != length:
            self.ser.reset_output_buffer()
            log_error = "error, sent less than {} bytes\n".format(length)
            print(log_error if self.logging else "", end="")
        else:
            log_error = "len: {}, pkt {}\n".format(length, buffer)
            print(log_error if self.logging else "", end="")


def main():
    pkt_counters = PacketCounters()
    itf_serial = InterfaceSerial(logging=True)
    while True:
        itf_serial.interface_write(pkt_counters)
        pkt_counters.packet_increment()
        time.sleep(2)


if __name__ == "__main__":
    main()
