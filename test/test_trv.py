import asyncio
import time
# from lightwave.lightwave import LWLink
from lightwave import LWLink


async def main():
    lwLink = LWLink('192.168.10.10')

    lwLink.set_trv_proxy("127.0.0.1", 8787)
    lwLink.set_temperature('R1Dh', 21, "Radiator")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
