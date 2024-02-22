"""
4. Advanced Protocols with Composition

Task: Define two protocols, JsonSerializable and XmlSerializable, and a composite protocol DataSerializable that
requires both JSON and XML serialization capabilities. Implement a class that adheres to DataSerializable.
"""

from typing import Protocol, Iterator


class JsonSerializable(Protocol):
    def to_json(self) -> str:
        """Return a JSON string representation of the object."""
        ...


class XmlSerializable(Protocol):
    def to_xml(self) -> str:
        """Return an XML string representation of the object."""
        ...


class DataSerializable(JsonSerializable, XmlSerializable, Protocol):
    """
    Composite protocol requiring JSON and XML serialization capabilities.

    Note that inheriting from an existing protocol does not automatically turn the subclass into a protocol – it just
    creates a regular (non-protocol) class or ABC that implements the given protocol (or protocols).

    --------------

    Similarly, explicitly assigning to a protocol instance can be a way to ask the type checker to verify that your class
    implements a protocol:

    _proto: SomeProto = cast(ExplicitSubclass, None)
    """
    pass


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def to_json(self) -> str:
        return f'{{"name": "{self.name}", "price": {self.price}}}'

    def to_xml(self) -> str:
        return f'<product><name>{self.name}</name><price>{self.price}</price></product>'


def check_serializable(obj: DataSerializable) -> Iterator[str]:
    """
    Iterator is more compatible here just in case it's easier to read
    But we can also specify Generator[int, None, None]
    """
    yield obj.to_json()
    yield obj.to_xml()


for i in check_serializable(Product("box", 100.00)):
    print(i)
