"""
9. Variadic Generics (Python 3.11+)

Task: create a move_first_element_to_last function that takes multiple that moves the first element to the end.
Use TypeVarTuple and Unpack (or *).

Note the use of the unpacking operator * in tuple[T, *Ts]. Conceptually, you can think of Ts as a tuple of type
variables (T1, T2, ...). tuple[T, *Ts] would then become tuple[T, *(T1, T2, ...)],
which is equivalent to tuple[T, T1, T2, ...].

(Note that in older versions of Python, you might see this written using Unpack instead, as Unpack[Ts].)
"""

from typing import TypeVar, TypeVarTuple

T = TypeVar("T")
Ts = TypeVarTuple("Ts")


def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return *tup[1:], tup[0]
