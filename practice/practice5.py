"""
5. Typed Context Managers

Task: Create a generic context manager class ResourcePool for managing resources like database connections.
Use generics to make it adaptable to different resource types and annotate the enter and exit methods accordingly.
"""

from contextlib import AbstractContextManager
from typing import Generic, TypeVar

# Define a type variable for the resource type
R = TypeVar('R')


class ResourcePool(AbstractContextManager, Generic[R]):
    def __init__(self, resource_factory):
        """
        Initialize the resource pool with a factory function that creates a new resource.
        """
        self.resource_factory = resource_factory
        self.resource: R = None

    def __enter__(self) -> R:
        """
        Enter the runtime context and acquire the resource.
        """
        if self.resource is None:
            self.resource = self.resource_factory()
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Exit the runtime context and release the resource.
        """
        # Implement resource release logic here.
        # This could involve closing a database connection, releasing a lock, etc.
        pass


def create_database_connection():
    # Placeholder for creating a database connection
    # In a real scenario, this would create and return a connection object
    return "database_connection"
