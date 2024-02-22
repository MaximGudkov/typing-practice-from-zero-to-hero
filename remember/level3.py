from typing import ClassVar


class MyClass:
    class_variable: ClassVar[int] = 10  # Class variable

    def __init__(self, instance_variable: int):
        self.instance_variable = instance_variable


instance = MyClass("20")  # Expected type 'int', got 'str' instead
instance2 = MyClass(20)  # Good
