#Import classes
from datetime import datetime
import shutil
import csv
import os
from os import path
from time import sleep
import socket
import struct

##Define variables used throughout the script##
#File containing list of networks
networks_file = ("networks.csv")
#File containing IPs of destination ASAs
devices_file = ("devices.csv")
#File containing final list of commands for ASA
cmd_file = ("commands.txt")
#ASA Parent Object Group Details
asa_object_group_name = ("RAVPN_EXCLUDE_NETWORKS")
asa_object_group_desc = ("This is the description of the object group")
#ASA Object Name 
asa_object_name = ("RAVPN_OBJECT_")
asa_object_desc = ("The is the description of the object name" )

#Define list of networks

#Convert CIDR to Subnet Mask Function
def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

#List of networks
networks_list = []

#Check to see if the source csv exists and add to list networks_list
if os.path.exists(networks_file):
    with open(networks_file, newline='') as f:
        reader = csv.reader(f)
        networks_list = list(reader)
    f.close()
else:
    print("The source file " + networks_file + " does not exist")

print(networks_list)

#Delete existing cmd_file
if os.path.exists(cmd_file):
    os.remove(cmd_file)

#Start adding commands
open_cmd_file = open(cmd_file,"a")
open_cmd_file.writelines("conf t\n object-group network" + asa_object_group_name + "\n desc " + asa_object_desc + "\n") 

#go through each network in the list and add the object to the command
for subnet in networks_list:
    cidr = 
    networkid = cidr_to_netmask(cidr)
    print(networkid)
    #open_cmd_file.writelines(subnet)

open_cmd_file.close()


