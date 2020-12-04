Networks2ASA 
2020/12/2 
Brian Dean 
brian@briandean.net 
--
Script to convert a list of networks a file to Cisco ASA Objects and add each of those objects to an object group. Update the config.ini, add your list of networks one per line, and run networks2asa.py. Output of commands in the commands file. Only subnet and host objects are supported with this script.

Change variables in config.ini to match your requirements.
networks_file = Path of file containing source networks networks to add to ASA as objects.
cmd_file = Path of output file with ASA commands
asa_object_group_name = Name of ASA object group
asa_object_group_desc = Description of the object group description with timestamp at the end
asa_object_name_prefix = Object names will put the asa_object_name_prefix variable in front of the IP address-prefix length. Example: ip address of 192.168.1.1 would be named "asa_object_name_prefix-192-168-1-1-32".
asa_object_desc = Description of each object with timestamp at the end.


networks_file = Source list of networks to be added to the ASA. Networks should be one per line. They can be in either CIDR notation or "network + subnet mask" or "network,subnet mask". Host addresses can either be as the ip address alone, /32, or ip address + 255.255.255.255.  MAKE SURE THERE ARE NOT ABNORMAL CHARACTERS IN THIS FILE.
Example valid networks file contents:  
192.168.0.0/24  
192.168.1.0 255.255.255.0  
192.168.2.0,/24  
192.168.3.0,255.255.255.0  
192.168.4.1  
192.168.4.2,/32  
192.168.4.3,255.255.255.255  
192.168.4.4 255.255.255.255  

convert2cidr.py = Script to normalize the formatting of the networks in the networks_file. This will create a backup of the original networks file in the same directory as .bak. You do not need to run this script individually.

networks2asa.py = Main script to convert list of networks to ASA commands and output to commands file. Will also run the convert2cidr.py.

commands file = File containing final commands to add networks as objects and add those objects to the object group on Cisco ASA  
Example output:  
conf t  
object network *Name of each object before IP address*-192-168-0-0-24  
 subnet 192.168.0.0 255.255.255.0  
 desc *Description of each object* 2020/12/02 09:42  
object-group network *Name of Object Group*  
 network-object object *Name of each object before IP address*-192-168-0-0-24  
object network *Name of each object before IP address*-192-168-4-4-32  
 host 192.168.4.4  
 desc *Description of each object* 2020/12/02 09:42  
object-group network *Name of Object Group*  
 network-object object *Name of each object before IP address*-192-168-4-4-32  
object-group network *Name of Object Group*  
 desc *Description for Object Group* 2020/12/02 09:42  
