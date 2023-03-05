# CARpwnd
Do it all tool for CAN-BUS Exploration, Enumeration and Exploitation

Written by ![CrashOverid3](https://github.com/CrashOverid3) and ![smadrid062](https://github.com/smadrid062)
# ToDo
- [x] Import MulticastUDP as Module
- [ ] Add ICSIM script?
- [ ] Add data abstraction modules
  - [x] dbc file conversion
  - [ ] matplotlib?
  - [ ] machine learning?
- [x] Make Public
  - [x] Finish Documentation
    - [x] Summary
    - [x] Installation
    - [x] Usage
    - [x] Modules
      - [x] Module Templates
    - [x] Spell and fact check
  - [x] test on windows
  - [x] create release
- [ ] Windows interface setup
- [ ] Make GUI front end for raspberry pi screen and infotainment uses

# Summary
CARpwnd is a colaborative project that is intended to be a framework for building automotive hacking tools.  There is a particular focus on the CAN bus but in theory anything can be added to it due to its dynamic loading of modules.  Modules can be added or removed at will allowing for very small package sizes to be installed on micro computers aslong as python is installed.  A majority of the base modules utilize [Python-Can](https://github.com/hardbyte/python-can) and hence are OS agnostic.  Windows and Linux specific modules are also included and will the user will be flaged if they are trying to run an incompatible module.  Contributions are welcomed and anything that is of value and isnt already included will be added to the main project.  
# Installation
Installation is easy and the only required dependencies currently are python-can and canutils.

For a Debian based system:
```
sudo pip install python-can
sudo apt install canutils
```
To download the repository
```
git clone https://github.com/CrashOverid3/CARpwned
```
The main carpwnd program will be in ./CARpwnd/carpwnd and can be run as an executable
```
cd ./CARpwnd
./carpwnd
```
![Carpwnd-version](https://user-images.githubusercontent.com/119644383/220784241-162628a8-9e38-4042-86dc-818966a70add.png)

# Usage
The execution of carpwnd is as follows ```./carpwnd <module> <submodule> [Options] <arguments>```

Example:```./carpwnd capture store -c can0 -e txt socketcan output.txt```
## Current Modules
### Injection
Injects individual CAN packets into the selected python-can supported interface
```
Usage: carpwnd injection [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  inject-frame  inject_frame will inject a can frame using the interface...
```
### Capture
Captures packets from a python-can supported interface and either dumps them to a file or the terminal
```
Usage: carpwnd capture [store, print] [OPTIONS] Interface OUTPUT_FILE

Options:
  -e, --extension-type [asc|blf|csv|db|log|txt]
                                  extension to use for output file
  -c, --channel TEXT              will give interface name to be identified by
  -v, --verbose                   ouput to stdout while writing to file
  -h, --help                      Show this message and exit.
```
### Convert
Converts database and captured interface formats to any other format supported by python-can and cantools.
```
Usage: carpwnd convert [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  tobus   Converts input file and sends it through the injector module
  tofile  Converts input file to a different format and writes to output
```
### Multicast
Simmilar to Capture but it sends and recieves packets over a multicast udp connection
```
Usage: carpwnd multicast [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  recieve  'multicast recieve' Command will recieve over udp multicast...
  send     'multicast send' Command will send can data over udp multicast
```
### Interface - Linux Only
Script that sets an interface up on a linux machine.  Does nothing if the machine is windows or macos.
```
Usage: carpwnd interface [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  setup  'can-type' The python-can compatible interface to setup
```
## Modules Template
Each module is just a seperate python file that is placed in the carpwnd-tools directory.  The file located at carpwnd/example-tool-template/example.py is a copy of the capture module with an excessive ammount of comments added to describe how it works.

The following is a general template of how modules in carpwnd are written.
```
#click argument parsing requirements for each module
@click.group()

#Set name for the click commands.  In this case its 'cli'
def cli():pass

#set first command
@cli.command()

#click options
@click.option("-e", "--example-option", help="example option")

#click arguments
@click.argument("example-argument")

#first module command that has the previous options and arguments
def example1(example_option, example_argument)
  #Module command help text
  """
  example help text
  """
  function contents...

#second command stuff
@cli.command()
@cli.option()
@cli.argument()
def example2()
  """
  help page
  """
  function contents...
```
