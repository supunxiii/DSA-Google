class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.root == None:
            return False
        else:
            return BinaryTree.preorder_search(self, self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = []
        BinaryTree.preorder_print(self, self.root, traversal)
        return '-'.join(traversal)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            left = BinaryTree.preorder_search(self, start.left, find_val)
            right = BinaryTree.preorder_search(self, start.right, find_val)
            return left or right
        else:
            return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""

        if start:
            value = start.value
            traversal.append(str(value))
            BinaryTree.preorder_print(self, start.left, traversal)
            BinaryTree.preorder_print(self, start.right, traversal)

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())