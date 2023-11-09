# this 'version' of our 'hello world' process uses asyncio Tasks to ensure that
# the calls to 'hello' are executed concurrently. 
# In this case this means that (when compared to the 'basic' example) this
# version should onlt take 2 seconds (as oppposed to 3 seconds).

import asyncio
import time

async def hello(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        hello(1, 'hello'))

    task2 = asyncio.create_task(
        hello(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())