#Capture Module with excessive notes to help others create modules themselves

#import Modules
import click
import datetime
import can 

#Setting File extensions to be used by the "-e" click option.
FILE_EXTENSION = ["asc","blf","csv","db","log","txt"]

#Setting a group in click so each module can be pulled back to the main project.
@click.group()

#setting the click command names.  **Note, The options and arguments for each command are still using 'click' not 'cli'
def cli():pass

#First click command with all of its options. Everything from here until the first function will be accosiated with it.
@cli.command()
#all of the options are not mandatory and have no order.
@click.option("-e","--extension-type", help="extension to use for output file", type=click.Choice(FILE_EXTENSION, case_sensitive=True))
@click.option("-v", "--verbose", help="ouput to stdout while writing to file", is_flag=True)
#all of the arguments are mandatory and passed in order that they are written here.
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True), default="log")
@click.argument("channel")
@click.argument("output-file")
#The first actual command.  The name of the function is what the command will be named in carpwnd.
#**Note, The options and arguments have '-' replaced with '_' when passed through.
def store(extension_type,verbose,bus_type,channel,output_file):
    #This is the description of the command.
    """
        'capture store'  command will dump can data into file specified

        output-file file to dump can data capture into
        
    """

    #Set a variable to track the ammount of packets captured.
    captured_total = 0
    #Combine the output file and extension type unless no extension type was provided.  Then, place it in the 'file_name' variable.
    file_name = f"{output_file}.{extension_type}" if extension_type else output_file
    #Set Python-can bus with type and channel
    bus = can.ThreadSafeBus(interface=bus_type, channel=channel) 
    #Create Python-can logger for writing packets to file.
    write_logger = can.Logger(file_name) if extension_type else open(file_name, "w")
    #if verbose option was called then dump all packets to terminal aswell
    if verbose:
        print_logger = can.Logger()
    #Create infinite loop for getting packets and writing them to file.
    while True:
        try:
            #get packet
            frame = bus.recv()
            if verbose:
                print_logger(frame)
            #Write packet to extension type
            if extension_type:
                write_logger(frame)
            #if extension type was not defined then dump to the same format as candump
            else:
                time =datetime.datetime.fromtimestamp(frame.timestamp)
                id = hex(frame.arbitration_id)
                frame_len = frame.dlc
                
                data = ' '.join(format(x, '02x') for x in frame.data)
                frame_str = f"({time}) {channel} {id} [{frame_len}] {data}"
                write_logger.write(frame_str)
        #Escape loop when user hits ctl+c     
        except click.exceptions.Abort:
            #Get the size in MB of the written output file and print for user
            file_size = can.io.canutils.CanutilsLogWriter.file_size(write_logger)
            print(f"\n{captured_total}\n{file_size}\tMB written to {file_name}")
            #Stop and close all of the loggers called
            if extension_type:
                write_logger.stop()
            else:
                write_logger.close()

            if verbose:
                print_logger.stop()
            break

    captured_total += 1

#The second click command.
@cli.command()
#Second commands arguments
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))
@click.argument("channel")
#The second actual command.
def print(bus_type, channel):
    """
    'capture print' will output the captured frames to stdout
    """
    logger = can.Printer()
    captured_total = 0
    bus = can.ThreadSafeBus(interface=bus_type, channel=channel)   
    while True:
        try:
            logger(bus.recv())
        except click.exceptions.Abort:
            print(f"{captured_total} captured frames")
            logger.stop()
            break

        captured_total += 1 
