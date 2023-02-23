import time
import can
import click
import sys
from can.interfaces.udp_multicast import UdpMulticastBus

@click.group()
def cli():pass

@cli.command()
@click.option("-c", "--channel", help="will give interface name to be identified by")
@click.argument("bus-type", type=click.Choice(can.VALID_INTERFACES, case_sensitive=True))
@click.argument("port", type=int, required=True)

def send(channel, bus_type, port):
    """
        'multicast send' Command will send can data over udp multicast

        'port'  Network port to use
    """
    with UdpMulticastBus(port=port) as udpbus, \
                         can.ThreadSafeBus(interface=bus_type, channel=channel) as hwrbus:
        buffer = can.BufferedReader()
        can.Notifier(hwrbus, [buffer])
        try:
            while True:
                msg = buffer.get_message()
                try:
                    udpbus.send(msg)
                except can.CanError:
                    print('MSG FAILED!')
        except KeyboardInterrupt:
            buffer.stop()
            print('Stopping...')
            pass

@cli.command()
#@click.option("-e","--extension-type", help="extension to use for output file", type=click.Choice(FILE_EXTENSION, case_sensitive=True), default="log")
#@click.option("-v", "--verbose", help="ouput to stdout while writing to file", is_flag=True)
@click.option("-c", "--channel", help="will give interface name to be identified by")
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))
@click.argument("port", type=int, required=True)
@click.argument("output-file")

def recieve(channel, bus_type, port, output_file):
    #file_name = f"{output_file}.{extension_type}"
    with UdpMulticastBus(port=port) as udpbus:
        write_logger = can.Logger(output_file)
        buffer = can.BufferedReader()
        can.Notifier(udpbus, [buffer])
        try:
            while True:
                msg = buffer.get_message()
                write_logger(msg)
        except KeyboardInterrupt:
            buffer.stop()
            print('Stopping...')
            pass