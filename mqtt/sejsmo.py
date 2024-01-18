import asyncio
import time 


class sejsmo:
    def __init__(self):
        self.sejsmo = 10

    def get_reads(self):
        return self.sejsmo + 10 * 1.5


async def print_sejsmo(sejsmo):
    while True:
        print(sejsmo.get_reads())
        time.sleep(3)
        await asyncio.sleep(3)

async def print_mandzio():
    while True:
        print("mandzio")
        await asyncio.sleep(1)


if __name__ == "__main__":
    reader = sejsmo()

    loop = asyncio.get_event_loop()
    loop.create_task(print_sejsmo(reader))
    loop.create_task(print_mandzio())

    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
