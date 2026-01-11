import time


def measure_time(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end - start


def fast_function():
    return sum(range(10))


def slow_function():
    time.sleep(0.1)
    return "done"


def run_tests():
    result, elapsed = measure_time(fast_function)
    assert result == 45
    assert elapsed >= 0

    result, elapsed = measure_time(slow_function)
    assert result == "done"
    assert elapsed >= 0.1

    print(" тести пройдено успішно ")


if __name__ == "__main__":
    run_tests()