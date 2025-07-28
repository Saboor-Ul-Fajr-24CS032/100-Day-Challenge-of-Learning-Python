# # Day 71 -> AsyncIO in python


import asyncio
import aiohttp
import time

async def func1(session):
    print("func 1 downloading...")
    url = "https://w0.peakpx.com/wallpaper/552/240/HD-wallpaper-gaming-wiki-good-gaming.jpg"
    async with session.get(url) as response:
        content = await response.read()
        with open("Image1.jpg", "wb") as f:
            f.write(content)
    print("Image1.jpg saved!")
    return 1

async def func2(session):
    print("func 2 downloading...")
    url = "https://e0.pxfuel.com/wallpapers/502/926/desktop-wallpaper-wiki-cool-2560x1080.jpg"
    async with session.get(url) as response:
        content = await response.read()
        with open("Image2.jpg", "wb") as f:
            f.write(content)
    print("Image2.jpg saved!")
    return 2

async def func3(session):
    print("func 3 downloading...")
    url = "https://www.nicepng.com/png/detail/850-8504261_deadpool-fox-battles-wiki-fandom-powered-wikia-deadpool.png"
    async with session.get(url) as response:
        content = await response.read()
        with open("Image3.jpg", "wb") as f:
            f.write(content)
    print("Image3.jpg saved!")
    return 3

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            func1(session),
            func2(session),
            func3(session),
        )
    end = time.time()

    print(f"Results: {results}")
    print(f"Execution time: {end - start:.2f} seconds")

asyncio.run(main())
