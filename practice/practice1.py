"""
1. Generic Containers with Constraints:

Task: Implement a generic LimitedList class that only accepts numbers (int or float) and has a limit on the number of
elements it can hold. Use type variables with bounds and constraints.
"""

from collections import UserList
from typing import Iterable


class LimitedList(UserList):
    def __new__(cls, iterable: Iterable, *args, **kwargs):
        is_valid = all(isinstance(val, int | float) for val in iterable)
        if not is_valid:
            raise TypeError("The list might contain only numbers (int, float)")
        return super().__new__(cls, iterable)

    def __init__(self, iterable, limit):
        super().__init__(iterable[:limit])
