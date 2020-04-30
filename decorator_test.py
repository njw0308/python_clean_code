# def test_decorator(func):
#     def function_wrapper(var):
#         print("Before calling " + func.__name__)
#         func(var)
#         print("After calling " + func.__name__)
#     return function_wrapper

# def be_decorated(var):
#     print("Hi, be_decorated func has been called with " + str(var))

# be_decorated = test_decorator(be_decorated)
# be_decorated("42")

# @test_decorator
# def be_decorated(var):
#     print("Hi, be_decorated func has been called with " + str(var))

# be_decorated("42")

# import time
# import threading

# def caculate_time(func):

#     def wrapper_func(*args, **kwargs):
#         start = time.perf_counter()
#         func(*args, **kwargs)
#         finish = time.perf_counter()
#         print(finish - start)
#         return func.__name__
    
#     return wrapper_func

# @caculate_time
# def test(*args, **kwargs):
#     sleep_time = kwargs.get('sleep_time', 1)
#     print("START")
#     time.sleep(sleep_time)
#     print("FINISTH")

# print(test())

from functools import wraps
import logging
logger = logging.getLogger(__name__)

def retry(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        error = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.warning("retrying %s", func.__qualname__)
                error = e
        raise error
    
    return wrapper_func

@retry
def run_something(*args, **kwargs):
    return sum(args)

print(run_something(1, 2))
print(run_something.__name__)

# 클래스 데코레이터

