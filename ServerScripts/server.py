#!/usr/bin/python

#
# @authors:
# @modified:
# @file: server.py
#
# This is script is to be run on the server computer (webserver).
# It is responsible for reciving status updates from displays
# on a pre-defined UDP port.
#
# Summary: 
# * Listening UDP Packets (status from clients)
# * Updating statuses based on time of contact
# * Sending UDP Packet to server for initialise connections
# * TCP connection for sending data or pictures or powerpoint

from socket import *
import sys
import time
import struct
import importlib

import pickle

BROADCAST_ADDRESS = '255.255.255.0'
PORT_LISTEN_DEVICES = 12345


class ServerDetect:
    def __init__(self):
        self.UDP_IP = ''
        self.UDP_PORT = PORT_LISTEN_DEVICES

        self.sock = socket(AF_NET, SOCK_DGRAM)
        self.sock.bind(('', PORT_LISTEN_DEVICES))

    def loop(self):
        while True:
            self.waitandrecv()
    

    def process_packet(self, addr, data):
        # the data is already decoded at this stage:
        server_name = data[0]
        server_ip = data[1]
        server_status = data[2]

        # check that the server IP is correct:
        print server_ip
        print addr

        


    def waitandrecv():
        # wait for packet to be received
        packet, addr = self.sockrecv.recv()

        # un-pickle the packet
        data = pickle.loads(packet)

        # process the data
        self.process_packet(self, data)
        


        




