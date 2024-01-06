#!/usr/bin/python3

import serial
import time
from ctypes import *
from enum import Enum

class Cfg(Enum):
    PKT_CNT_INFO = 0x01
    SYN_MRK_INFO = 0xEFBEADDE
    SER_PRT_INFO = '/dev/ttyUSB0'
    SER_BUD_INFO = 115200

class Packet(Structure):
    _pack_ = 1
    _fields_ = [
            ("sync_marker", c_uint),
            ("packet_length", c_uint),
            ("packet_apid", c_uint),
            ("x_counter", c_ubyte),
            ("y_counter", c_ubyte)]

    def inc_cnts(self):
        self.x_counter = self.x_counter + 1
        self.y_counter = self.y_counter + 2

    def serialize(self):
        return bytearray(self)

    def pkt_len(self):
        return len(bytearray(self))


def main():

    ser = serial.Serial(Cfg.SER_PRT_INFO.value, Cfg.SER_BUD_INFO.value)
    pkt = Packet(Cfg.SYN_MRK_INFO.value, 6, Cfg.PKT_CNT_INFO.value, 0, 0)

    while True:

        bytes_written = ser.write(pkt.serialize())

        if bytes_written != pkt.pkt_len():
            print("error, only sent {} bytes of {}".format(
                bytes_written, pkt.pkt_len()))

        print("len: {}, pkt: {}".format(pkt.pkt_len(), pkt.serialize()))

        pkt.inc_cnts()
        time.sleep(2)


if __name__ == "__main__":
    main()
