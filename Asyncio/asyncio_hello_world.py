# A 'helo world' like introduction to the use of 'asyncio' - based on the examples from 
# 'Real Python' - https://realpython.com/async-io-python/. For more info look at
# https://docs.python.org/3/library/asyncio-task.html

import asyncio
import time

# define a 'hello' function that waits for the specified time and then  prints the string that was passed
# a function declared with the async / await syntax is known as a 'coroutine'
async def hello(delay, what):
    print("hello starting ....")
    await asyncio.sleep(delay)
    print(what)

# the 'top-level' entry point
async def main():
    print(f"started at {time.strftime('%X')}")

    # awaiting on a coroutine - ensures that 'hello' is printed
    # before 'world'
    await hello(1, 'hello')
    await hello(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# use 'asyncio.run()' to execute the top-level entry point.
asyncio.run(main())