#Import libs
import fileinput
import sys
#Removes commas, spaces, and converts subnet mask to cidr number

def convert(x):
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(' ', ''), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(',', ''), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.255', '/32'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.254', '/31'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.252', '/30'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.248', '/29'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.240', '/28'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.224', '/27'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.192', '/26'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.128', '/25'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.255.0', '/24'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.254.0', '/23'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.252.0', '/22'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.248.0', '/21'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.240.0', '/20'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.224.0', '/19'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.192.0', '/18'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.128.0', '/17'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.255.0.0', '/16'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.254.0.0', '/15'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.252.0.0', '/14'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.248.0.0', '/13'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.240.0.0', '/12'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.224.0.0', '/11'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.192.0.0', '/10'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.128.0.0', '/9'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('255.0.0.0', '/8'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('254.0.0.0', '/7'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('252.0.0.0', '/6'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('248.0.0.0', '/5'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('240.0.0.0', '/4'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('224.0.0.0', '/3'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('192.0.0.0', '/2'), end='')
    with fileinput.FileInput(x, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('128.0.0.0', '/1'), end='')

#Uncomment the below two lines if you want to run this script on its own. Use "python convert2cidr.py *filename*"
#filename = sys.argv[1]
#convert(filename)