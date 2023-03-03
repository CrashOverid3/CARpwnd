import click 
import platform
import subprocess
import can
import os

def run_cmd(cmd):
    subprocess.run(cmd.split(), stdout=subprocess.DEVNULL)


@click.group()
def cli():pass

@cli.command()
@click.option("-b", "--bit-rate", help="Sets the speed of the interface", type=int, default=0)
@click.argument("can-type",type=click.Choice(can.VALID_INTERFACES, case_sensitive=True))
@click.argument("channel")
def setup(can_type, channel, bit_rate):
    '''
    'can-type' The python-can compatible interface to setup

    'channel' The channel to set the interface as
    '''
    if (os_version := platform.system()) == "Linux":
        if can_type == "vcan":
            run_cmd(f"sudo modprobe {can_type}")
        if channel in os.listdir('/sys/class/net/'):
            run_cmd(f"sudo ip link down {channel}")
            run_cmd(f"sudo ip link set {channel} type {can_interface} bitrate {bit-rate}")
            run_cmd(f"sudo ip link up {channel}")
        else:
            if bitrate != 0:
                run_cmd(f"sudo ip link add {channel} type {can_interface} bitrate {bit-rate}")
            else: 
                run_cmd(f"sudo ip link add {channel} type {can_interface}")

            run_cmd(f"sudo ip link up {channel}")

    if (os_version := platform.system()) == "Darwin":
       pass
    if (os_version := platform.system()) == "Windows":
       pass
