import time


def speed_calc_decorator(function):
    def function_wrapper():
        time_before = time.time()
        function()
        time_after = time.time()
        print(f"{function.__name__} run speed: {time_after - time_before}")

    return function_wrapper


def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


if __name__ == "__main__":
    fast_fun_decorated = speed_calc_decorator(fast_function)
    fast_fun_decorated()

    slow_function()
