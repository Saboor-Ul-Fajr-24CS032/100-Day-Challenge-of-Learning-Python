Day 71 -> AsyncIO in python



AsyncIO in python:
Async IO in Python lets your program run tasks without waiting for one to finish before starting another. It uses the asyncio module.
Functions are written with async def, and you use await for tasks like delays or I/O (downloading, reading).
asyncio.gather() runs multiple async tasks concurrently.
In my code, each func downloads an image, and with gather(), all three download at the same time, so it’s faster than doing them one by one.

aiohttp:
A Python library used for asynchronous HTTP requests (downloading data, APIs, etc.).
Unlike requests, it’s non-blocking, meaning multiple downloads can run at the same time.
It always used with asyncio.

