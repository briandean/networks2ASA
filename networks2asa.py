#Import libs
from datetime import datetime
import csv
import os
from ipaddress import IPv4Network
import convert2cidr
import configparser

#Get timestamp to use in the commands
now = datetime.now()
now_str = now.strftime("%Y/%m/%d %H:%M")

#Config parser
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

#File containing list of networks
networks_file = (config['DEFAULT']['networks_file'])
#File containing final list of commands for ASA
cmd_file = (config['DEFAULT']['cmd_file'])
#ASA Parent Object Group Details
asa_object_group_name = (config['DEFAULT']['asa_object_group_name'])
asa_object_group_desc = (config['DEFAULT']['asa_object_group_desc'] + " " + now_str)
#ASA Object Name 
asa_object_name_prefix = (config['DEFAULT']['asa_object_name_prefix'] + "-")
#ASA Object description. Might break this out to the csv import in the future
asa_object_desc = (config['DEFAULT']['asa_object_desc'] + " " + now_str)

#Run convertocidr.py script
convert2cidr.convert(networks_file)

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

#Uncomment this to print the list of networks in the console
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
print("Done!")
