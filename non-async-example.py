import time

def my_func_1():
    print("Starting my_func_1...")
    time.sleep(5)  # This simulates a non-blocking delay
    print("my_func_1 finished")
    return 5

def my_func_2():
    print("Starting my_func_2...")
    time.sleep(5)  # This simulates a non-blocking delay
    print("my_func_2 finished")
    return 10


def main():
    x = my_func_1()
    y = my_func_2()

    print(f"Result from my_async_func_1: {x}")
    print(f"Result from my_async_func_2: {y}")

if __name__ == '__main__':
    main()