# Local libraries
import asyncio

# Third party libraries
from tracers.function import trace


@trace
async def function_a():
    await trace(asyncio.sleep)(0.1)
    await function_b()


@trace
async def function_b():
    await trace(asyncio.sleep)(0.1)
    await function_c()
    await trace(asyncio.sleep)(0.1)
    await function_d()
    await trace(asyncio.sleep)(0.1)
    await function_e()


@trace
async def function_c():
    await trace(asyncio.sleep)(0.1)
    await function_d()


@trace
async def function_d():
    await trace(asyncio.sleep)(0.1)


@trace
async def function_e():
    await trace(asyncio.sleep)(0.1)


async def main():
    await asyncio.gather(*[
        asyncio.create_task(function_a()),
        asyncio.create_task(function_b()),
    ])


if __name__ == '__main__':
    asyncio.run(main())