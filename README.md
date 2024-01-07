# RPI Telemetry Tester

A simple cosmos plugin that receives telemetry from a raspberry pi 4.

## Resources

- [OpenC3 Documentation](https://openc3.com)
- [Python Library "ctypes"](https://docs.python.org/3/library/ctypes.html)
- [Python Library "pyserial"](https://pyserial.readthedocs.io/en/latest/)

## Getting Started

```bash
# RPI SETUP
> dmesg -wH # plugin raspberrypi confirm device (e.g. /dev/ttyUSB0) is created
> ping <ip> # wait for boot complete, then ping rpi for aliveness
> chmod 666 <device> # (e.g. /dev/ttyUSB0) allows cosmos container access to device

# COSMOS SETUP
> mkdir ~/cosmos && cd ~/cosmos
> git clone https://github.com/OpenC3/cosmos-project.git # clone project starter
> cd cosmos-project/

# Add device fd (e.g. /dev/ttyUSB0) to openc3-operator node in compose.yaml
    devices:
        - "/dev/ttyUSB0:/dev/ttyUSB0"

# Comment out demo app in .env file
    #OPENC3_DEMO=1

# RPI PLUGIN SETUP
# Clone down my cosmos plugin inside ~/cosmos/cosmos-project/
> git clone https://github.com/rogueWookie/openc3-cosmos-rpi.git
> ./openc3 run # start cosmos containers
> google-chrome --app=http://localhost:2900 # open cosmos page
# load/install gem file, scp over target_app/app.py to RPI, start it
```

## Reminders & Remaining Tasks

1. Edit the .gemspec file fields: name, summary, description, authors, email, and homepage
1. Update the LICENSE.txt file with your company name
