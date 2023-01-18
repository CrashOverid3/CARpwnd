#Written by Dade M. AKA CrashOveride
#Find More information on what I am working on at https://www.crashoveride.info
#This tool is intended to be a "Do it all" for CAN-BUS Enumeration, Discovery and Exploitation

#Import Modules
import can
import random
import argparse
from Modules.Reader import R2File
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
arguments.add_argument('-M', '--Module', help = 'Select Program module to use', choices = ['Reader','Injector'])
arguments.add_argument('-o', '--Output', help = 'Output file into current directory')
arguments.add_argument('-i', '--Input', help = 'Input file from current directory')
arguments.add_argument('-I', '--Interface', help = 'Manually select CAN interface. Example: socketcan', choices = ['canalystii','cantact','etas','gs_usb','iscan','ixxat','kvaser','neousys','neovi','nican','nixnet', 'robotell','seeedstudio','serial','slcan','socketcan','socketcand','systec','udp_multicast','usb2can','vector','virtual'])
arguments.add_argument('-C', '--Channel', help = 'Manually select CAN Channel. Example: vcan0')
arguments = arguments.parse_args()
#main()