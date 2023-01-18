#Written by Dade M. AKA CrashOveride
#Find More information on what I am working on at https://www.crashoveride.info
#This Module is designed to dump the CAN interface into various file formats

#Import Modules
import can
#Log Interface to file chosen by user until keyboard interrupt 
def main(output, interface, channel):  
    with can.ThreadSafeBus(interface=interface, channel=channel) as bus:
        logger = can.Logger(output)
        try:
            print('Dumping to '+output+'. Press Ctl+C to stop...')
            while True:        
                logger(bus.recv())
        except KeyboardInterrupt:
            print()
            print(str(can.io.canutils.CanutilsLogWriter.file_size(logger)/1024/1024)+' MegaBytes written to '+output)
            logger.stop()
            pass
    return()
def desc(): #This can probably be done a better way
    desc='''
    This Module dumps the CAN interface to whatever the output variable is set to
    '''
    return(desc)