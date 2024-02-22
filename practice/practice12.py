"""
12. Annotating Callbacks and Higher-Order Functions

Task: Annotate a higher-order function apply_to_list that takes a list and a callback function, applies the callback to
each element of the list, and returns a new list. Ensure type safety between the input list, callback, and output list.
"""

from typing import TypeVar, Callable

T = TypeVar('T')
R = TypeVar('R')


def apply_to_list(lst: list[T], callback: Callable[[T], R]) -> list[R]:
    return [callback(item) for item in lst]
