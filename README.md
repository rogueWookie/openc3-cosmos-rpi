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
> scp openc3-cosmos-rpi/targets/RPI/target_apps/app.py <user>@<ip>:/home/<user>

# START COSMOS & RPI APP
> ./openc3 run # start cosmos containers
> google-chrome --app=http://localhost:2900 # create password
> google-chrome --app=http://localhost:2900/tools/admin # load/install rpi plugin gem
> ssh <user>@<ip> # log in to rpi execute app <./app.py>
```

## Reminders & Remaining Tasks

- Edit the .gemspec file fields: name, summary, description, authors, email, and homepage
- Add a yocto recipe for pulling down the app.py and installing it
