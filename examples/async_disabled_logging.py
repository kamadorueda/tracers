# Local libraries
import asyncio

# Third party libraries
from tracers.function import call, trace


# This function has logging enabled
#   all downstream functions will be logged too regardless of their log_to.
# Only the top-level log_to is taken into account
@trace()
async def function_a():
    await call(asyncio.sleep, 0.1)
    await function_b()


# This automatically disables all downstream tracers
#   (it means functions b to e will not be logged)
@trace(log_to=None)
async def function_b():
    await call(asyncio.sleep, 0.1)
    await function_c()
    await call(asyncio.sleep, 0.1)
    await function_d()
    await call(asyncio.sleep, 0.1)
    await function_e()


@trace()
async def function_c():
    await call(asyncio.sleep, 0.1)
    await function_d()


@trace()
async def function_d():
    await call(asyncio.sleep, 0.1)


@trace()
async def function_e():
    await call(asyncio.sleep, 0.1)


async def main():
    await asyncio.gather(*[
        asyncio.create_task(function_a()),
        asyncio.create_task(function_b()),
    ])


if __name__ == '__main__':
    asyncio.run(main())
