#Written for CARpwnd
#This is an example Module that is meant to be a easy to modify template
#for CARpwnd

#Import Modules
import can
#The main() function is what is called during normal module execution.
#This Example is from the R2File module. ThreadSafeBus is the preffered
#BUS read/writer because it can be used at the same time as other modules.
def main(interface, channel, output):
    with can.ThreadSafeBus(interface=interface, channel=channel) as bus:
        logger = can.Logger(output)
        PacketTotal = 0
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
#The desc() function is called when more information is required on module usage and execution
def desc():
    desc='''
This is the description of the Module that is shown at Module selection.
    '''
    return(desc)
#The options() function is called right before execution to make sure all required
#variables are set.  Anything that is not in the following list will have to be
#entered by the user manually after selection or set during Module execution.  This set of
#"Other" module options should be set in the secon list of the options tuple
#Global Options = [interface, channel, input, output] 
def options():
    options = [['interface', 'channel', 'output'],['filesize']]
    return(options)