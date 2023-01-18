#Written by Dade M. AKA CrashOveride
#Find More information on what I am working on at https://www.crashoveride.info
#This tool is intended to be a "Do it all" for CAN-BUS Enumeration, Discovery and Exploitation

#Import Modules
import can
import random
import argparse
from Modules.Reader import *
#from Modules.Injector import * 

#Set CANBUS Variables

#Set terrible puns
punsfile = open('Openings/Puns.txt')
ASCIIfile = open('Openings/ASCII.txt')
#Manual Overide for testing############
#output='test.csv'
#interface='socketcan'
#channel='vcan0'
#R2File.main(output, interface, channel)
#######################################



def main():
    print(punsfile.readlines()[random.randrange(0,2)]) #Should make this check how many lines are in the file.
    #print(ASCIIfile)

#Set and parse arguments for better scripting
arguments = argparse.ArgumentParser()
arguments.add_argument('-M', '--Module', help = 'Select program module to use.')
arguments.add_argument('-L', '--List', help = 'List avalible modules.', action='store_true')
arguments.add_argument('-o', '--Output', help = 'Output file into current directory.')
arguments.add_argument('-i', '--Input', help = 'Input file from current directory.')
arguments.add_argument('-I', '--Interface', help = 'Manually select CAN interface. Example: socketcan', choices = ['canalystii','cantact','etas','gs_usb','iscan','ixxat','kvaser','neousys','neovi','nican','nixnet', 'robotell','seeedstudio','serial','slcan','socketcan','socketcand','systec','udp_multicast','usb2can','vector','virtual'])
arguments.add_argument('-C', '--Channel', help = 'Manually select CAN Channel. Example: vcan0')
arguments = arguments.parse_args()
#Check for ListModules argument and display before starting program
if arguments.List:
    with open('Modules/Reader/__init__.py','r') as f:
        print('Loaded Reader Modules: '+f.read()[10:])
    with open('Modules/Injector/__init__.py','r') as f:
        print('Loaded Injection Modules: '+f.read()[10:])
        quit()

#main()