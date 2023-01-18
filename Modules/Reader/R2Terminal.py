#Written for CARpwnd
#This Module is designed to dump the CAN channel into the terminal

#Import Modules
import can
import time
#dump channel to file chosen by user until keyboard interrupt 
def main(interface, channel):  
    with can.ThreadSafeBus(interface=interface, channel=channel) as bus:
        logger = can.Logger(None)
        PacketTotal = 0
        try:
            print('Dumping to the terminal. Press Ctl+C to stop...')
            time.sleep(0.5)
            while True:        
                logger(bus.recv())
                PacketTotal = PacketTotal + 1
        except KeyboardInterrupt:
            print()
            print(str(PacketTotal)+' Packets Dumped')
            logger.stop()
            pass
    return()
def info(): #This can probably be done a better way
    desc='''
    This Module dumps the CAN channel into the terminal until a keyboard interupt.
    '''
    return(desc)