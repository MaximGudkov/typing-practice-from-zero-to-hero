from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def first[T](seq: Sequence[T]) -> T:  # Function is generic over the TypeVar "T"
    return seq[0]
