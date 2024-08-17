import asyncio


async def my_async_func_1():
    print("Starting my_async_func_1...")
    await asyncio.sleep(5)  # This simulates a non-blocking delay
    print("my_async_func_1 finished")
    return 5


async def my_async_func_2():
    print("Starting my_async_func_2...")
    await asyncio.sleep(5)  # This simulates a non-blocking delay
    print("my_async_func_2 finished")
    return 10


async def main():
    task1 = asyncio.create_task(my_async_func_1())  # Create the first task
    task2 = asyncio.create_task(my_async_func_2())  # Create the second task

    # Await both tasks to run concurrently
    x = await task1
    y = await task2

    print(f"Result from my_async_func_1: {x}")
    print(f"Result from my_async_func_2: {y}")

if __name__ == '__main__':
    asyncio.run(main())  # Running the async main function