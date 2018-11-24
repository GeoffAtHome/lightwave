import asyncio
import time
from lightwave.lightwave import LWLink


async def main():
    lwLink = LWLink('192.168.15.226')

    print("Off")
    # R1D3 is room 1 device 3
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
