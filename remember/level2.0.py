from collections.abc import Sequence


def first[T](seq: Sequence[T]) -> T:  # T can be used without import
    return seq[0]
