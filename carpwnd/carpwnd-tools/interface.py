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
@click.argument("name")
def setup(can_type, name, bit_rate):
    '''
    'can-type' The python-can compatible interface to setup

    'NAME' The name to set the interface as
    '''
    if (os_version := platform.system()) == "Linux":
        if can_type == "vcan":
            run_cmd(f"sudo modprobe {can_type}")
        if name in os.listdir('/sys/class/net/'):
            run_cmd(f"sudo ip link down {name}")
            run_cmd(f"sudo ip link set {name} type {can_interface} bitrate {bit-rate}")
            run_cmd(f"sudo ip link up {name}")
        else:
            if bitrate != 0:
                run_cmd(f"sudo ip link add {name} type {can_interface} bitrate {bit-rate}")
            else: 
                run_cmd(f"sudo ip link add {name} type {can_interface}")

            run_cmd(f"sudo ip link up {name}")

    if (os_version := platform.system()) == "Darwin":
       pass
    if (os_version := platform.system()) == "Windows":
       pass
