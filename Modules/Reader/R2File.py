#Written for CARpwnd
#This Module is designed to dump the CAN interface into various file formats

#Import Modules
import can
#Log Interface to file chosen by user until keyboard interrupt 
def main(ModuleOptions, output, interface, channel):  
    with can.ThreadSafeBus(interface=interface, channel=channel) as bus:
        logger = can.Logger(output)
        PacketTotal = 0
        print(ModuleOptions)
        try:
            print('Dumping to '+output+'. Press Ctl+C to stop...')
            while True:        
                logger(bus.recv())
                PacketTotal = PacketTotal + 1
        except KeyboardInterrupt:
            print()
            print(str(PacketTotal)+' Packets Recorded')
            print(str(can.io.canutils.CanutilsLogWriter.file_size(logger)/1024/1024)+' MegaBytes written to '+output)
            logger.stop()
            pass
    return()
def info():
    desc='''
    This Module dumps the CAN interface to whatever the output file is set to.
    '''
    return(desc)
def options():
    options = ['Interface', 'Channel', 'Output'],['Filesize']
    return(options)