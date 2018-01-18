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
