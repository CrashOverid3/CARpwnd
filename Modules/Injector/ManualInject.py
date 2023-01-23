#Written for CARpwnd
#This Module is designed to inject CAN packets based on user inputs
#Import Modules
import can
#Ask users for message info and send message on BUS
def main(ModuleOptions, interface, channel):  
    ModuleOptions.split(',')
    with can.ThreadSafeBus(interface=interface, channel=channel) as bus:
        msg = can.message(
            arbitration_id=ModuleOptions[0],
            data=ModuleOptions[1])
    return()
def info():
    desc='''
    This Module asks for input and injects it onto the CAN-Bus
    '''
    return(desc)
def options():
    options = ['Interface', 'Channel'],'arbitrarion_id,data'
    return(options)