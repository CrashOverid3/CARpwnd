import click
import datetime
import can 

FILE_EXTENSION = ["asc","blf","csv","db","log","txt"]

@click.group()
def cli():pass

@cli.command()
@click.option("-e","--extension-type", help="extension to use for output file", type=click.Choice(FILE_EXTENSION, case_sensitive=True))
@click.option("-v", "--verbose", help="ouput to stdout while writing to file", is_flag=True)
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True), default="log")
@click.argument("channel")
@click.argument("output-file")

def store(extension_type,verbose,bus_type,channel,output_file):
    """
        'capture store'  command will dump can data into file specified

        bus-type        the type of CAN interface you want to use to send frames
        channel         the python-can interface name to capture frames from     
        output-file     file to dump can data capture into
        
    """
    captured_total = 0
    file_name = f"{output_file}.{extension_type}" if extension_type else output_file
    bus = can.ThreadSafeBus(interface=bus_type, channel=channel) 
    write_logger = can.Logger(file_name) if extension_type else open(file_name, "w")
    if verbose:
        print_logger = can.Logger()
    while True:
        try:
            frame = bus.recv()
            if verbose:
                print_logger(frame)
            if extension_type:
                write_logger(frame)
            else:
                time =datetime.datetime.fromtimestamp(frame.timestamp)
                id = hex(frame.arbitration_id)
                frame_len = frame.dlc
                
                data = ' '.join(format(x, '02x') for x in frame.data)
                frame_str = f"({time}) {channel} {id} [{frame_len}] {data}"
                write_logger.write(frame_str)                
        except click.exceptions.Abort:
            file_size = can.io.canutils.CanutilsLogWriter.file_size(write_logger)
            print(f"\n{captured_total}\n{file_size}\tMB written to {file_name}")
            if extension_type:
                write_logger.stop()
            else:
                write_logger.close()

            if verbose:
                print_logger.stop()
            break
    captured_total += 1

@cli.command()
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))
@click.argument("channel")

def print(bus_type, channel):
    """
    'capture print' will output the captured frames to stdout

    bus-type        the type of CAN interface you want to use to send frames
    channel         the python-can interface name to capture frames from     
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