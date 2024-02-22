from typing import Callable

ReturnIntFunc = Callable[..., int]


def decorator(func: ReturnIntFunc) -> ReturnIntFunc:
    def wrapper(*args, **kwargs) -> int:
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator
def sum_nums(*nums):
    return sum(nums)
