"""
6. Annotating Decorators that Change Signatures

Task: Write a decorator that changes the signature of the decorated function
(e.g., adds an argument or changes the return type) and correctly annotate the decorator using Callable.
"""

from functools import wraps
from typing import Callable, TypeVar

ReturnType = TypeVar('ReturnType')
RFunc = Callable[..., ReturnType]


def add_argument(func: RFunc) -> RFunc:
    @wraps(func)
    def wrapper(*args, **kwargs) -> ReturnType:
        return func(*args, "Added argument", **kwargs)

    return wrapper
