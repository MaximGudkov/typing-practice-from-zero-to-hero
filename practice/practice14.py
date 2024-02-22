"""
14. Annotating Recursive Functions and Data Structures

Task: Create a recursive data structure (e.g., a binary tree) and a function that operates on it
(e.g., searches for a value). Annotate both the data structure and the function to ensure type safety.
"""

from typing import Optional, TypeVar, Generic

T = TypeVar('T')


class TreeNode(Generic[T]):
    def __init__(self, value: T, left: 'Optional[TreeNode[T]]' = None, right: 'Optional[TreeNode[T]]' = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def search_tree(node: Optional[TreeNode[T]], target: T) -> bool:
    if node is None:
        return False
    if node.value == target:
        return True
    # Recursively search in the left and right subtrees
    return search_tree(node.left, target) or search_tree(node.right, target)


# Create a simple binary tree
#       1
#      / \
#     2   3
root = TreeNode(1, TreeNode(2), TreeNode(3))

# Search for different values in the tree
print(search_tree(root, 2))  # Output: True
print(search_tree(root, 4))  # Output: False
