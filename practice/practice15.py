"""
15. Type Checking Dynamically Created Classes
Task: Dynamically create a class (e.g., using type() or metaclasses) that includes type-annotated methods or properties.
Demonstrate how to ensure these dynamic classes are type-checked.
"""

from typing import Protocol


def dynamic_method(self, value: int) -> str:
    return f"Value: {value}"


# Dynamically create a class with a type-annotated method
DynamicClass = type('DynamicClass', (object,), {'dynamic_method': dynamic_method})


class DynamicClassProtocol(Protocol):
    def dynamic_method(self, value: int) -> str: ...


# Use the protocol as a type hint for instances of the dynamic class
def use_dynamic_class(instance: DynamicClassProtocol) -> None:
    print(instance.dynamic_method(10))


dynamic_instance = DynamicClass()
use_dynamic_class(dynamic_instance)  # This should pass type checking
