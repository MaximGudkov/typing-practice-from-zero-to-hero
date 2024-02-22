"""
3. Custom Type Guards

Task: Write a custom type guard function is_numeric that can differentiate between numeric (int or float) and
non-numeric types at runtime and use it to narrow types in a function that handles mixed-type lists.
"""

from typing import List, Any


def is_numeric(value: Any) -> bool:
    """Custom type guard function to check if a value is numeric (int or float)."""
    return isinstance(value, (int, float))


def sum_numeric_values(values: List[Any]) -> float:
    """Sum up numeric (int or float) values in a mixed-type list."""
    total = 0.0  # Use a float to accommodate both int and float values in the sum
    for value in values:
        if is_numeric(value):
            # The type checker understands that `value` is either int or float here,
            # thanks to the `is_numeric` type guard.
            total += value  # Safe to add value since it's confirmed to be numeric
    return total


mixed_list = [1, 2.5, "Python", 3, "Type Hints", 4.5]

# The function processes the mixed_list and sums up only the numeric values.
total_sum = sum_numeric_values(mixed_list)
print(total_sum)  # Output: 11.0 (1 + 2.5 + 3 + 4.5)
