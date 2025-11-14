# binary_search_tree.py

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, items):
        # The first item initializes the root
        self.root = TreeNode(items[0])
        # Insert remaining items
        for item in items[1:]:
            self._insert(self.root, item)

    def _insert(self, node, value):
        """Recursively insert into the correct subtree."""
        if value <= node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:  # value > node.data
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def data(self):
        """Return the root node of the tree."""
        return self.root

    def sorted_data(self):
        """Return an in-order traversal (sorted list)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)
