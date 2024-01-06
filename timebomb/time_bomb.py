import asyncio
import random

async def time_bomb(min_time=5, max_time=60, exploded_flag=None):
    if min_time > max_time:
        raise ValueError("min_time must be less than or equal to max_time")

    time_to_explosion = random.randint(min_time, max_time)
    print(f"Time Bomb set for {time_to_explosion} seconds!")

    await asyncio.sleep(time_to_explosion)
    print('Boom!')
    if exploded_flag is not None:
        exploded_flag[0] = True  # Set the flag to indicate the bomb has exploded
