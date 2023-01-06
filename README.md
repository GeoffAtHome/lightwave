# lightwave
Python library to provide a reliable communication link with LightWaveRF lights, switches and TRVs.

# Installation
Either clone this repository and run `python setup.py install`, or install from pip using `pip install lightwave`.

## API
This library makes use of the public API provided by lightwave that can be found here: https://api.lightwaverf.com/lighting_power.html
# Lights and Switches
The library supports the following functions:
```
turn_on_light(device_id, name)
turn_on_switch(device_id, name)
turn_on_with_brightness(device_id, name, brightness)
turn_off(device_id, name)
```
Where:
* **device_id** takes the form **R#D#** where **R#** is the room number and **D#** is the device number.
* **name** is the text that will be displayed on the hub.
* **brightness** is a value from 0 (off) to 255 (full on).

## Usage
Initialise a link to the hub by passing in the IP address required. Then call a method on the object to modify the device.
The first time a switch is turned on or off the device will attempt to pair to the hub. This should then show a message on your WiFi Link asking you to pair the device. You have 12 seconds to push the button on the WiFi Link to accept this.


```
import asyncio
import time
from lightwave.lightwave import LWLink

async def main():
    lwLink = LWLink('192.168.15.226')

    print("Off")
    ### R1D3 is room 1 device 3
    lwLink.turn_off('R1D3', "Wall Lights")
    lwLink.turn_off('R1D4', "Ceiling Lights")

    time.sleep(5)
    print("On")
    lwLink.turn_on_light('R1D3', "Wall Lights")
    lwLink.turn_on_light('R1D4', "Ceiling Lights")

    time.sleep(5)
    print("Off")
    lwLink.turn_off('R1D3', "Wall Lights")
    lwLink.turn_off('R1D4', "Ceiling Lights")


    time.sleep(5)
    print("On")
    lwLink.turn_on_with_brightness('R1D3', "Wall Lights", 25)
    lwLink.turn_on_with_brightness('R1D4', "Ceiling Lights", 50)
    lwLink.turn_on_switch('R1D1', "Sockets one")
    lwLink.turn_on_switch('R1D2', "Sockets two")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```
# TRV Support
The library also supports TRVs with the following function:
```
set_temperature (device_id, temp, name)
```
Where:
* **device_id** takes the form **R#D#** where **R#** is the room number and **D#** is the device identifier (normally **Dh**).
* **temp** is the target temperature (0.5 increments)
* **name** is the text that will be displayed on the hub.
## TRV Proxy
The Proxy is now optional.  A built in listener is now available via the async function ```LW_listen()```.

Alternativly, to read the TRV status (current temperature, target_temperature, battery status and current output) a [Lightwave TRV Proxy](https://github.com/ColinRobbins/Homeassistant-Lightwave-TRV) can be used. 
To use the proxy:
```
set_trv_proxy (proxy_ip, proxy_port)
(temp, targ, batt, output) = read_trv_status(serial)
```
Where:
* **proxy_ip** is the IP address of the proxy
* **proxy_port** is the IP Port of the proxy
* **serial** is the serial number of the TRV of interest (NB: This is the **serial** number, and NOT **device_id** they are different).
# Contributors
* TRV Support by [Colin Robbins](https://github.com/ColinRobbins)
