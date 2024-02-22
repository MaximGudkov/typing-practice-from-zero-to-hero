from typing import TypeVar, Generic

T = TypeVar('T')


class ItemContainer(Generic[T]):  # or just class ItemContainer[T] (python >= 3.10)
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item


# Usage examples
int_container = ItemContainer[int](123)
str_container = ItemContainer[str]("Hello")

print(int_container.get_item())  # Output: 123
print(str_container.get_item())  # Output: Hello
