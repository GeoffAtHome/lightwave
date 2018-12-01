import asyncio
import time
# from lightwave.lightwave import LWLink
from lightwave import LWLink


async def main():
    lwLink = LWLink('192.168.15.226')

    print("Off")
    # R1D3 is room 1 device 3
    lwLink.turn_off('R2D1', "Wall Lights")
    lwLink.turn_off('R2D2', "Ceiling Lights")

    time.sleep(5)
    print("On")
    lwLink.turn_on_light('R2D1', "Wall Lights")
    lwLink.turn_on_light('R2D2', "Ceiling Lights")

    time.sleep(5)
    print("Off")
    lwLink.turn_off('R2D1', "Wall Lights")
    lwLink.turn_off('R2D2', "Ceiling Lights")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
