# CARpwnd
Do it all tool for CAN-BUS Exploration, Enumeration and Exploitation

Written by @github/CrashOverid3 and @github/smadrid062
# ToDo
- [x] Import MulticastUDP as Module
- [ ] Add ICSIM script?
- [ ] Add data abstraction modules
  - [ ] matplotlib?
  - [ ] machine learning?
- [ ] Make Public
  - [ ] Finish Documentation
  - [ ] test on windows
  - [ ] create release
# Summary
CARpwnd is a colaborative project that is intended to be a framework for building automotive hacking tools.  There is a particular focus on the CAN bus but in theory anything can be added to it due to its dynamic loading of modules.  Modules can be added or removed at will allowing for very small package sizes to be installed on micro computers aslong as python is installed.  A majority of the base modules utilize [Python-Can](https://github.com/hardbyte/python-can) and hence are OS agnostic.  Windows and Linux specific modules are also included and will the user will be flaged if they are trying to run an incompatible module.
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
# Module Teplates
