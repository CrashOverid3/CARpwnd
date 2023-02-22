# CARpwned
Do it all tool for CAN-BUS Exploration, Enumeration and Exploitation

Written by @github/CrashOverid3 and @github/smadrid062
# ToDo
- [ ] Import MulticastUDP as Module
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
# Usage

# Module Teplates
