# TimeBomb Module

This module exports a function `time_bomb` which, when called in an asyncio environment, will schedule the termination of the Python process after a random time interval. The time interval is customizable by the user.

## Usage

You can use the `time_bomb` function by specifying the minimum and maximum time in seconds. If these parameters are not provided, it defaults to a random time between 5 seconds and 1 minute. In an asyncio context, you can check for the explosion event and exit the loop accordingly.

```python
import asyncio
from timebomb.time_bomb import time_bomb

async def main():
    exploded_flag = [False]  # A mutable container to hold the exploded flag
    asyncio.create_task(time_bomb(min_time=2, max_time=4, exploded_flag=exploded_flag))

    # Infinite loop
    print("Starting infinite loop")
    while not exploded_flag[0]:  # Check if the bomb has exploded
        print("Looping...")
        await asyncio.sleep(1)

    print("Bomb has exploded. Exiting loop.")

# Run the async main function
asyncio.run(main())
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
