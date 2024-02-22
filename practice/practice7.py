"""
7. Type Inference with Generators

Task: Implement a generator function fibonacci that yields an infinite sequence of Fibonacci numbers.
Use type hints to indicate the generator's return type and utilize the function in a type-safe manner.


The type hint Generator[int, None, None] indicates that this generator yields integers (int), doesn't expect any value
to be sent into the generator, and doesn't return any final value when it's exhausted (which, in this case,
it never will be since it's infinite).
"""

from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
