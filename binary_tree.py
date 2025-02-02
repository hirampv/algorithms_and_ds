class binaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self, value):
        new_node = binaryTreeNode(value)
        self.root = new_node