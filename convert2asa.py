#Import libs
from datetime import datetime
import csv
import os
from os import path
from time import sleep
from ipaddress import IPv4Network

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
asa_object_name_prefix = ("RAVPN_OBJECT_")
#ASA Object description. Might break this out to the csv import in the future
asa_object_desc = ("The is the description of the object name" ) 

#Define list of networks
networks_list = []

#Check to see if the source csv exists and add to list networks_list
if os.path.exists(networks_file):
    with open(networks_file, newline='') as f:
        reader = csv.reader(f)
        networks_list = list(reader)
    f.close()
else:
    print("The source file " + networks_file + " does not exist")

# print(networks_list)

#Delete existing cmd_file
if os.path.exists(cmd_file):
    os.remove(cmd_file)

#Start adding commands
open_cmd_file = open(cmd_file,"a")
open_cmd_file.writelines("conf t\n")
#Go through each network in the list and add the object to the command
for x in networks_list:
    network = str(IPv4Network(x[0]).network_address)
    netmask = str(IPv4Network(x[0]).netmask)
    cidr = str(IPv4Network(x[0]).prefixlen)
    asa_object_name = asa_object_name_prefix + str.replace(network, ".", "-") + "-" + cidr
    # asa_object_desc = str(x[1])
    #print(network,netmask)
    if netmask == '255.255.255.255':
        open_cmd_file.writelines("object network "+ asa_object_name + "\n host " + network + "\n desc " + asa_object_desc + "\n")
    else:
        open_cmd_file.writelines("object network "+ asa_object_name + "\n subnet " + network + " " + netmask + "\n desc " + asa_object_desc + "\n")
    open_cmd_file.writelines("object-group network " + asa_object_group_name + "\n network-object object " + asa_object_name + "\n")

#Add description to the object group at the end
open_cmd_file.writelines("object-group network " + asa_object_group_name + "\n desc " + asa_object_group_desc + "\n") 

#Close the command file
open_cmd_file.close()


