import click 
import platform
import subprocess
import can
import os

def run_cmd(cmd):
    subprocess.run(str(cmd).split(), stdout=subprocess.DEVNULL)

@click.group()
def cli():pass

@cli.command("can-type",type=click.Choice(can.interface), case_sensitive=True)
@click.argument("name")
@click.option("-b", "--bit-rate", type=click.INT, default=0)
#@click.argument()
def change_interface(can_type,name,bit_rate):
    
    if (os_version == platform.system()) is "Linux":
        if can_type is "vcan":
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

    if (os_version := platform.system()) is "Darwin":
       pass
    if (os_version := platform.system()) is "Windows":
       pass