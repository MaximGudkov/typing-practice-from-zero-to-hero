"""
10. Type Narrowing with Literal Types

Task: Use Literal types to define a function configure_mode that accepts specific string literals
("light", "dark", or "auto") and configures an application's theme accordingly. Demonstrate type narrowing based
on these literals.

Literals containing two or more values are equivalent to the union of those values. So, Literal[-3, b"foo", MyEnum.A]
is equivalent to Union[Literal[-3], Literal[b"foo"], Literal[MyEnum.A]]. This makes writing more complex types involving
literals a little more convenient.

Literal types may also contain None. Mypy will treat Literal[None] as being equivalent to just None. This means that
Literal[4, None], Union[Literal[4], None], and Optional[Literal[4]] are all equivalent.

----------------

Literals may also contain aliases to other literal types. For example, the following program is legal:

PrimaryColors = Literal["red", "blue", "yellow"]
SecondaryColors = Literal["purple", "green", "orange"]
AllowedColors = Literal[PrimaryColors, SecondaryColors]

def paint(color: AllowedColors) -> None: ...

paint("red")        # Type checks!
paint("turquoise")  # Does not type check
"""

from typing import Literal

Mode = Literal["light", "dark", "auto"]


def configure_mode(mode: Mode) -> None:
    if mode == "light":
        print("Configuring theme to light mode.")
    elif mode == "dark":
        print("Configuring theme to dark mode.")
    else:
        print("Configuring theme to automatic mode based on system settings.")
