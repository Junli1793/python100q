#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Async IO in Python: A Complete Walkthrough: https://realpython.com/async-io-python/

asyncio is a library to write concurrent code using the async/await syntax.

a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.

"""
import asyncio

print()
print("==============Example 1==============")


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()
