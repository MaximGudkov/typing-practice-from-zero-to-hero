from typing import List, Dict, Tuple, Set, Optional

a: int = 1
b: bool = True
c: str = "a"
d: float = 1.1


def greet(name: str) -> str:
    return f"Hi, {name}"


e: list = [1, 2, 3]
e2: List = [1, 2, 3]
e3: list[int] = [1, 2, 3]

f: dict = {"a": 1}
f2: Dict = {"a": 1}
f3: Dict[str, int] = {"a": 1}
f4: Dict[str, int | str] = {"a": 1, "b": "2"}

g: tuple = (1, 2, 3)
g2: Tuple = (1, 2, 3)
g3: tuple[int, str, int] = (1, "2", 3)
g4: tuple[int, ...] = (1, 2, 3)


def name_and_age(name: str, age: int) -> tuple[str, int]:
    return name, age


h: set = {1, 2, 3}
h2: Set = {1, 2, 3}
h3: set[int] = {1, 2, 3}
h4: set[int | str] = {1, "2", 3}

l: Optional[int] = None if 1 else 1

Point = tuple[int, int]
type Point2 = tuple[int, int]


def print_point(point: Point) -> None:
    print(point[0], point[1])
