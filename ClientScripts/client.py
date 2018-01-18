#!/usr/bin/python

#
# @authors:
# @modified:
# @file: client.py
#
# This is script is to be run on the computer attached to the
# displays.  It is responsible for sending out status updates
# on a pre-defined UDP port.
#
# Summary: 
# * Sending UDP Packets (name, ip, status)
# * Listen for UDP Packets (ip, <data>)
# * Bind to TCP packets for reciecing data or pictures or powerpoints
# * Close connection
import socket
import pickle
port = 12345
broadcastAddress = '255.255.255.255'
name = 'clientMeme'


class ClientComms:
    """
    A Custom Socket Server that sends UDP packets to the screen manager to give the
    status of the RPi on the network
    """

    def __init__(self):
        self.UDP_IP = broadcastAddress
        self.UDP_PORT = port
        self.socksend = socket.socket(socket.AF_INET,  # Internet
                                      socket.SOCK_DGRAM)  # UDP
        data = [name,broadcastAddress,port]
        self.packer = pickle.dumps(data)

        print("[INFO] Client has packed the data and transmitted on (broadcastAddress:port)")

    def send(self, throttle, steering):
        # encode the values into an array
        val = (round(throttle, 2), round(steering, 2))

        # pack the values into the right format
        data = self.packer.pack(*val)

        # send the data over the UDP socket.
        self.socksend.sendto(data, (self.UDP_IP, self.UDP_PORT))

if __name__ == '__main__':
    try:
        # uncomment for spammer
        #spam = Spammer()
        #spam.generate()

        # uncomment for AI
    except KeyboardInterrupt:
        exit(0)
