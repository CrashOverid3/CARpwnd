#Written by Dade M. AKA CrashOveride
#Find More information on what I am working on at https://www.crashoveride.info
#This tool is intended to be a "Do it all" for CAN-BUS Enumeration, Discovery and Exploitation

#Import Modules
import can
import random
import argparse
from Modules.Reader import *
from Modules.Injector import * 
from os import listdir, system
from time import sleep
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
    ModulesLoaded = ListModules()
    if arguments.Module:
        result = any(arguments.Module in sublist for sublist in ModulesLoaded[0])
        if result == True:                
            Module = arguments.Module
        else:
            print('Module selection "'+arguments.Module+'" is invalid. Append -L to list avalible modules')
            quit()
    else:
        Module = SelectModule(ModulesLoaded)
    system('clear')
    print('Executing '+Module+'...')
    #globals()[str(Module)].main(interface, channel)

def ListModules():
    ModuleCatagories = listdir(path='./Modules')
    ModulesLoaded = []
    n = -1
    for Catagory in ModuleCatagories:
            n = n + 1
            ModulesLoaded.append(listdir(path='./Modules/'+Catagory))
            ModulesLoaded[n].remove('__init__.py')
            ModulesLoaded[n].remove('__pycache__') #<-------Annoying
            ModulesLoaded[n] = [s.replace('.py','') for s in ModulesLoaded[n]]
    print('''
Loaded Modules by Catagory
--------------------------''')
    n = 0
    for Catagory in ModuleCatagories:
        print(ModuleCatagories[n])
        print(ModulesLoaded[n])
        n = n + 1
    sleep(1)
    return([ModulesLoaded, ModuleCatagories])     

def SelectModule(ModulesLoaded):
    system('clear')
    print('''
Select a Catagory From Below
--------------------------''')
    n = 0
    for Catagory in ModulesLoaded[1]:
        print(str(n+1)+': '+Catagory)
        n = n + 1
    Catagory = int(input())-1
    system('clear')
    print('''
Select a Module From Below
--------------------------''')
    n = 0
    for Module in ModulesLoaded:
        print(str(n+1)+': '+ModulesLoaded[0][Catagory][n])
        n = n + 1
    Module = ModulesLoaded[0][Catagory][int(input())-1]
    return(Module)

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