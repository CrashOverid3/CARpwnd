#Example carpwnd module writen to help others understand how to write modules

#import modules
import can
import time
#all modules require at the very least click
import click

#ANSI colors
white = '[95m'
black = '[94m'
red = '[96m'
green = '[92m'
blue = '[93m'
endc = '[0m'

#set list of choices for first command option
colors = ['white', 'black', 'red', 'green', 'blue']

#set click group that carpwnd pulls from to get the module commands
@click.group()
def cli():pass

#set first command
@cli.command()
#set options for first command
@click.option("-c", "--channel", help="will give interface name to be identified by")

#set arguments for first command
#@click.argument("color", type=click.Choice(colors, case_sensitive=True))
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))

def colorprint(channel, color, bus_type):
    """
    'example colorprint' will output the captured frames to stdout in COLOR!
    """
    buffer = can.BufferedReader()
    captured_total = 0
    bus = can.ThreadSafeBus(interface=bus_type, channel=channel) if channel is not None else can.ThreadSafeBus(interface=bus_type)
    
    while True:
        try:
            msg = buffer.get_message
            print(f"{color}{msg} {endc}")
        except KeyboardInterrupt:
            print(f"{color}{captured_total} captured frames {endc}")
            logger.stop()
            break

        captured_total += 1 

#set second command
@cli.command()
#set options for second command
@click.option("-c", "--channel", help="will give interface name to be identified by")

#set arguments for second command
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))

def print(channel, bus_type):
    """
    'example print' will output the captured frames to stdout
    """
    logger = can.Printer()
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