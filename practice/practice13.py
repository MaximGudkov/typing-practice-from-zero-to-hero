"""
13. Structural Subtyping with TypedDict

Task: Use TypedDict to create a type for a complex JSON structure expected from an API response. Write a function that
accepts such a structure and safely extracts data from it.
"""

from typing import TypedDict


class UserResponse(TypedDict):
    name: str
    age: int
    interests: list[str]


def process_user_response(response: UserResponse) -> None:
    # Extract data from the response
    name = response["name"]
    age = response["age"]
    interests = response["interests"]

    # Process the data (for demonstration, we'll just print it)
    print(f"Name: {name}, Age: {age}, Interests: {', '.join(interests)}")


user_response: UserResponse = {
    "name": "Alice",
    "age": 30,
    "interests": ["Reading", "Cycling", "Hiking"]
}

process_user_response(user_response)
