# 🌳 Simple Binary Tree Implementation
# Author: Aashi Asati
# Hacktoberfest 2025
# Description: Build a basic binary tree and traverse it in-order

class Node:
    """A node in the binary tree."""
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Binary Tree with basic insert and traversal methods."""
    def _init_(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, parent, value):
        """Insert a node to the left of the given parent node."""
        if not parent.left:
            parent.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = parent.left
            parent.left = new_node

    def insert_right(self, parent, value):
        """Insert a node to the right of the given parent node."""
        if not parent.right:
            parent.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = parent.right
            parent.right = new_node

    def inorder_traversal(self, node):
        """Print the nodes of the tree in in-order fashion."""
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

def main():
    print("🌟 Welcome to the Binary Tree Demo 🌟")

    # Create a tree with root value 10
    tree = BinaryTree(10)

    # Insert nodes like a human would logically do
    tree.insert_left(tree.root, 5)
    tree.insert_right(tree.root, 15)
    tree.insert_left(tree.root.left, 3)
    tree.insert_right(tree.root.left, 7)

    # Display the tree
    print("\nIn-order Traversal of the Binary Tree:")
    tree.inorder_traversal(tree.root)
    print("\n✅ Done!")

if _name_ == "_main_":
    main()
