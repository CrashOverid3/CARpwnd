import click
import time
import can 


FILE_EXTENSION = ["asc","blf","csv","db","log","txt"]

@click.group()
@click.command()
def cli():pass

@cli.command()
@cli.option("-e","--extension-type", help="extension to use for output file", type=click.Choice(FILE_EXTENSION, case_sensitive=True), default="log")
@cli.option("-c", "--channel", help="will give interface name to be identified by")
@cli.option("-v", "--verbose", help="ouput to stdout while writing to file", is_flag=True)
@cli.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))
@cli.argument("output-file", type=click.path)
def store_capture(extension_type,channel,verbose,bus_type,output_file):
    """
        store capture  command will dump can data into file specified

        output-file file to dump can data capture into
    """
    captured_total = 0
    file_name = f"{output_file}.{extension_type}"
    bus = can.ThreadSafeBus(interface=bus_type, channel=channel) if channel is not None else can.ThreadSafeBus(interface=bus_type)
    write_logger = can.Logger(file_name)
    if verbose:
        print_logger = can.Logger()
    while True:

        try:
            frame = bus.recv()
            if verbose:
                print_logger(frame)
            write_logger(frame)
        except KeyboardInterrupt:
            file_size = can.io.canutils.CanutilsLogWriter.file_size(write_logger)
            print(f"\n{captured_total}\n{file_size}\tMB written to {file_name}")
            write_logger.stop()
            if verbose:
                print_logger.stop()
            break

    captured_total += 1

@cli.command()
@cli.option("-c", "--channel", help="will give interface name to be identified by")
@cli.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))
def print_capture(channel, bus_type):
    """
    print-capture will output the captured frames to stdout
    """
    logger = can.Logger()
    captured_total = 0
    bus = can.ThreadSafeBus(interface=bus_type, channel=channel) if channel is not None else can.ThreadSafeBus(interface=bus_type)
    
    while True:
        try:
            logger(bus.recv())
        except KeyboardInterrupt:
            print(f"{captured_total} captured frames")
            logger.stop()
            break

        captured_total += 1 
