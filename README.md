# lightwave
Python library to provide a realiable communication link with LightWaveRF lights and switches.

# Installation
Either clone this resposition and run `python setup.py install`, or install from pip using `pip install lightwave`.

# API
This library makes use of the public API provided by lightwave that can be found here: https://api.lightwaverf.com/lighting_power.html
# Usage
Initialise a link to the hub by passing in the IP address required. Then call a method on the object to modify the device.
The first time a switch is turned on or off the device will attempt to pair to the hub. This should then show a message on your WiFi Link asking you to pair the device. You have 12 seconds to push the button on the WiFi Link to accept this.