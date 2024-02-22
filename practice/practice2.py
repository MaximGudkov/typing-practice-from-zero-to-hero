"""
2. Covariant and Contravariant Generics

Task: Create a generic Processor class with a method process and demonstrate covariance and contravariance with respect
to input and output types.

when using TypeVar the default values of parameters covariant=False, contravariant=False. This means that the actual
value is
    INVARIANT and with provided example I can only use Animal when creating Processor[Animal, str](get_sound)
if covariant=True:
    COVARIANT and with provided example I can use Animal AND all its SUBCLASSES e.g. Dog, Cat when creating Processor[Dog, str](get_sound)
if contravariant=True:
    CONTRAVARIANT and with provided example I can use SUPERCLASSES AND e.g. Object when creating Processor[Object, str](get_sound)


from docs:

By default, mypy assumes that all user-defined generics are invariant. To declare a given generic class as covariant or
contravariant use type variables defined with special keyword arguments covariant or contravariant. For example:

from typing import Generic, TypeVar


class Animal:
    def speak(self):
        return "Some generic animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


T_co = TypeVar('T_co', covariant=True)


class Box(Generic[T_co]):  # this type is declared covariant
    def __init__(self, content: T_co) -> None:
        self._content = content

    def get_content(self) -> T_co:
        return self._content


def look_into(box: Box[Animal]): ...


my_box = Box(Cat())
look_into(my_box)  # OK, but mypy would complain here for an invariant type
"""

from typing import TypeVar, Callable

# Define type variables with covariant and contravariant bounds
T_co = TypeVar('T_co', covariant=True)  # T_co can be substituted with a subtype
T_contra = TypeVar('T_contra', contravariant=True)  # T_contra can be substituted with a supertype


class Processor[T_contra, T_co]:
    def __init__(self, process_func: Callable[[T_contra], T_co]):
        self.process_func = process_func

    def process(self, item: T_contra) -> T_co:
        return self.process_func(item)


class Animal:
    def speak(self):
        return "Some generic animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# A function that processes Animals and returns their sounds
def get_sound(animal: Animal) -> str:
    return animal.speak()


# A Processor that accepts an Animal (or its subclasses) and returns a string
animal_sound_processor = Processor[Animal, str](get_sound)

# Using the processor with a Dog instance
dog = Dog()
print(animal_sound_processor.process(dog))  # Output: Woof!

# Using the processor with a Cat instance
cat = Cat()
print(animal_sound_processor.process(cat))  # Output: Meow!
