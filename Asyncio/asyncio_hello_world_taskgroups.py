# the prefered way to execute concurrent 'tasks' (since Python 3.11) is to make use of
# task groups

import asyncio
import time

async def hello(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            hello(1, 'hello'))

        task2 = tg.create_task(
            hello(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())