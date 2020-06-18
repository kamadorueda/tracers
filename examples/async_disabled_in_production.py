# Local libraries
import asyncio

# Third party libraries
from tracers.function import trace


# Constants
PRODUCTION: bool = True


# This top-level function will be traced intentionally
@trace
async def function_a():
    await trace(asyncio.sleep)(0.1)
    await function_b()


# This automatically disables all downstream tracers
#   (it means functions b to e will not be traced)
@trace(do_trace=not PRODUCTION)
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