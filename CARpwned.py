#Written by Dade M. AKA CrashOveride
#Find More information on what I am working on at https://www.crashoveride.info
#This tool is intended to be a "Do it all" for CAN-BUS Enumeration, Discovery and Exploitation

#Import Modules
import os.path as path
from os import getcwd, getuid
import os
import subprocess
import sys
import getopt
import random
import time
import argparse

punsfile = open('Openings/Puns.txt')
ASCIIfile = open('Openings/ASCII.txt')
uid = 0
#Check if user has admin access in order to enable CAN interfaces.
if getuid() > 1:
    uid = 1
    print('*You need to run this as root for maximum funcionality*')
time.sleep(1)
#Opening Function for ASCII art and Puns
def OpeningASCII(file):
    num = random.randrange(0,1)
    #dade use string.split(@)
def Openingpuns():
    print(OpeningASCII(ASCIIfile))
    print(punsfile.readlines()[random.randrange(0,2)]) #Should make this check how many lines are in the file.
    time.sleep(1.5)

def Opening(interface):
    if interface == False:
        interface = detectif() #Set a tuple for the current (interface, state(Empty or False))
        if interface == False:
            userinput = input('There are no CAN interfaces Detected.  Enter an interface to start [vcan0, can0]:') #Make this setup real CAN someday
            if userinput == 'vcan0' or 'can0':
                setupvcan(uid, interface=userinput)
            else:
                quit()
        elif len(interface) > 1:
            userinput = input('Interface detected but it is down.  Do you want to start it? ['+interface[0]+']:')
            if userinput == 'y':
                print('Setting interface state to UP')
                if uid == 1:
                    print('You need admin access to enable an interface!')
                    time.sleep(2)
                    quit()
                else:
                    subprocess.Popen('sudo ip link set up '+interface[0]+'',shell = True, stdout = subprocess.PIPE)
            else:
                quit()
        else:
            time.sleep(1.5)
            return interface[0]
    else:
        print('gotomodule')
#Detect Interface name and state using linux "ip link" command
def detectif():
    print('Detecting CAN interface...')
    ifname = str(subprocess.Popen('ip link | grep can',shell = True, stdout = subprocess.PIPE).communicate())
    ifstate = str(subprocess.Popen('ip link | grep -E "can.*DOWN"',shell = True, stdout = subprocess.PIPE).communicate())
    if ifname[6:10] == 'can0':
        output = [ifname[6:10]]
        print('Interface can0 Found!')
        if ifstate[6:10] == 'can0':
            output.append(1)
        else:
             output.append(0)
    elif ifname[6:11] == 'vcan0':
        output = [ifname[6:11]]
        print('Interface vcan0 Found!')
        if ifstate[6:11] == 'vcan0':
            output.append(1)
        else:
             output.append(0)
    else:
        output = False #Leads to option of enabling CAN interface
        if output == False:
            print('Interface Not Found...')
    time.sleep(1.5)
    return output #make it parse lines for command to check for interface? | Make it OS/command Agnostic?

#Enable vcan0 interface. *requires admin access
def setupvcan(uid, interface):
    if interface == False:
        interface = input('Would you like to start a CAN interface?: [can0, vcan0, n]')
    if interface == 'vcan0' or 'can0':
        if uid == 1:
            print('You need admin access to enable an interface!')
            time.sleep(2)
            quit()
        else:
            print('Starting Virtual CAN Interface...')
            subprocess.Popen('sudo modprobe can',shell = True, stdout = subprocess.PIPE)
            subprocess.Popen('sudo modprobe vcan',shell = True, stdout = subprocess.PIPE)
            subprocess.Popen('sudo ip link add dev '+interface+' type vcan',shell = True, stdout = subprocess.PIPE)
            subprocess.Popen('sudo ip link set up '+interface+'',shell = True, stdout = subprocess.PIPE)
            print('ICSIM is still needed to make this virtual interface useful') #Possibly integrate ICSIM?
            userinput = input('Would you like to start ICSIM on vcan0?:')
            if userinput == 'y':
                print('icsim start')
                return interface
            elif userinput == 'n':
                print('Continueing with active but empty interface')
                return interface
            else:
                print('please connect an active interface or select to start ICSIM to continue.')
                quit()
            time.sleep(2)
            selectmod()
    else:
        quit()
    
def readif(interface, inputfile, outputfile):
    os.system('clear')
    print('Interface selected ['+interface+']')
    userinput = input('''
    Read Interface >
    ------------------------------------
        1: Write interface into file
        2: Output to terminal
        3:
        4:
        5: Return to Previous screen
    ------------------------------------
        (Add -h or --help for info on options)
    Selection: ''')
    if userinput == '1':
        print('Write to file')
        print(str(inputfile))
    elif userinput == '2':
        print('write to terminal')
    elif userinput == '5':
        selectmod(interface)
#Main Program for yes
def selectmod(interface, inputfile, outputfile):
    os.system('clear')
    print('Interface Selected ['+interface+']')
    userinput = input('''
        Options Avalible:
        ------------------------------------
        1: Select Different Interface
        2: Read Interface
        3:
        4:
        ------------------------------------
        (Add -h or --help for info on options)
        Selection: ''')
    if userinput == '1':
        print('Interface changing will be implimented soon')
    elif userinput == '2':
        readif(interface, inputfile, outputfile)

#Check for arguments in case they want to not use menus because 1337 Hax0r
parser = argparse.ArgumentParser()
parser.add_argument('-M', '--Module', help = 'Select Program module to use', choices = ['Reader','Injector'])
parser.add_argument('-o', '--Output', help = 'Output file into current directory ['+getcwd()+'/]')
parser.add_argument('-i', '--Input', help = 'Input file from current directory ['+getcwd()+'/]')
parser.add_argument('-I', '--Interface', help = 'Manually select CAN interface')
args = parser.parse_args()
#Set arguments to variables 
if args.Interface:
    interface = args.Interface
else:
    interface = False
if args.Module:
    module = args.Module
else:
    module = False
if args.Input:
    inputfile = args.Input
else:
    inputfile = False
if args.Output:
    outputfile = args.Output
else:
    outputfile = False
#Check if inputs were parsed and determine flow of program
Openingpuns()
Opening(interface)
if module == False:
    selectmod(interface, inputfile, outputfile)
elif module == 'Reader':
    readif(interface, inputfile, outputfile)
else:
    print('other module chosen')
