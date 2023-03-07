import click
import can
import sys
import os
import time

@click.group()
def cli():pass

@cli.command()
@click.option("-p", "--period", help="periodicaly send frame. period specified in seconds", type=click.FLOAT)
@click.option("-d", "--duration", help="how many time to send frame. ignored if no value set for period", type=click.INT)
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))
@click.option("--channel")
@click.argument("arbitration-id")
@click.argument("data", nargs=-1)
def inject_frame(period, duration,bus_type,channel, arbitration_id, data):
    """ 
        inject_frame will inject a can frame using the interface type selected 

        ex. 
            socketcan 0xC0FFEE 0 25 0 1 3 1 4 1 
        
        bus-type        the type of CAN interface you want to use to send frames
        channel         the interface name 
        arbitration-id  the id to use when sending data on frame 

    """
    bus = can.ThreadSafeBus(interface=bus_type, channel=channel)
    try:
        msg = can.Message(arbitration_id=arbitration_id,data=data.split(), check=True)
    except ValueError:
        print("invalid data input", file=sys.stderr)
        sys.exit(-1)
    
    if period is not None:
        try:
            bus.send_periodic(msg,period=period, duration=duration) if duration != 0 else bus.send_periodic()
        except click.exeption.Abort:
            bus.stop()
    else:
        bus.send(msg)     

@cli.command()
@click.argument("bus-type",type=click.Choice(can.VALID_INTERFACES,case_sensitive=True))
@click.argument("channel")
@click.argument("input-file", type=click.Path())


def replay_dump(bus_type, input_file, channel):
    """
    replay_dump will inject all of the packets on a dump file into the interface


    """
    bus = can.ThreadSafeBus(interface=bus_type, channel=channel)
    input_file = open(input_file).readlines()
    for i in input_file:
        packets = []
        data = i.split(':')
        packets.append(data[1][1:18])
        packets.append('0x'+data[2][2:5])
        packets.append(data[3][7:30])
        array = bytearray.fromhex(packets[2])
        try:
            print(f"Sending {packets[1]} {packets[2]}")
            msg = can.Message(arbitration_id=int(packets[1],16),data=array, check=True, is_extended_id=False)
            bus.send(msg)
        except ValueError:
            print('error')
            sys.exit(-1)

        time.sleep(0.001)
    print('Packets Sucessfully Sent!')
