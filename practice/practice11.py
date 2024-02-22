"""
11. Advanced Union and Intersection Types

Task: Create functions that demonstrate the use of advanced union and intersection type constructs to handle complex
data structures that can be one of several types or must satisfy multiple type constraints simultaneously.

from docs:

About @overload:
When you use overload, you provide several "dummy" definitions of a function, each with a different type signature.
These definitions are not executed. Then, you provide a final, concrete implementation, which does not have the
@overload decorator. The concrete implementation is the one that runs, and it's responsible for handling the actual
logic for all the overloaded cases.

About @runtime_checkable:
The runtime_checkable decorator, also from the typing module, is used with Protocol classes to make them suitable for
runtime isinstance and issubclass checks. By default, protocols are only used for static type checking and don't support
these runtime checks. When you decorate a Protocol with @runtime_checkable, it allows you to use isinstance and
issubclass with instances and classes that implement the protocol, respectively.
"""

from typing import Protocol, overload, runtime_checkable, NoReturn


class HasName(Protocol):
    name: str


class HasAge(Protocol):
    age: int


@runtime_checkable  # OTHERWISE: TypeError: Instance and class checks can only be used with @runtime_checkable protocols
class HasAgeName(HasName, HasAge, Protocol):
    pass


@overload
def get_person_info(person: HasAgeName) -> str: ...


@overload
def get_person_info(person: str) -> NoReturn: ...  # just to practice NoReturn (can be used when error will be raised)


def get_person_info(person):
    if isinstance(person, HasAgeName):
        return f"Name: {person.name}, Age: {person.age}"
    raise TypeError("person must have both name and age")
