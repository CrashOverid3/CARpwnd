#Written by Dade M. AKA CrashOveride
#Find More information on what I am working on at https://www.crashoveride.info
#This tool is intended to be a "Do it all" for CAN-BUS Enumeration, Discovery and Exploitation

#Import Modules
import can
import random
import argparse
from Modules.Reader import *
from Modules.Injector import * 
from os import listdir

#Set globals of imported modules


#Set CANBUS Variables

#Set terrible puns
punsfile = open('Openings/Puns.txt','r')
ASCIIfile = open('Openings/ASCII.txt','r')
#Manual Overide for testing############
#output='test.csv'
#interface='socketcan'
#channel='vcan0'
#R2File.main(output, interface, channel)
#######################################

def main():
    print(ASCIIfile.read().split("@NEWLINE@")[random.randrange(0,2)])
    print(punsfile.readlines()[random.randrange(0,2)]) #Should make this check how many lines are in the file.
    #Load Modules into tuple and check if module argument was called and valid
    LoadedModules = ListModules()
    #print(LoadedModules)
    if arguments.Module:
        result = any(arguments.Module in sublist for sublist in LoadedModules)
        if result == True:                
            module = arguments.Module
        else:
            print('Module "'+arguments.Module+'" Invalid. Append -L to list avalible Modules')
            quit()
    else:
        module = SelectModule()
    globals()[str(module)].main(interface, channel)

def ListModules():
    ModuleCatagories = listdir(path='./Modules')
    ModulesLoaded = []
    n = -1
    for Module in ModuleCatagories:
            n = n + 1
            ModulesLoaded.append(listdir(path='./Modules/'+Module))
            ModulesLoaded[n].remove('__init__.py')
            ModulesLoaded[n].remove('__pycache__') #<-------Annoying
    print('''
Loaded Modules by Catagory
--------------------------''')
    n = -1
    for Module in ModuleCatagories:
        n = n + 1
        print(ModuleCatagories[n])
        print(ModulesLoaded[n])
    return(ModulesLoaded)
        

def SelectModule():
    return('SelectModule')
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
    ListModules()
    quit()

main()