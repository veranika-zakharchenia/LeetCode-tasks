import random


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        root = self.root
        while root:
            if val > root.info:
                if not root.right:
                    root.right = Node(val)
                    return
                root = root.right
            elif val <= root.info:
                if not root.left:
                    root.left = Node(val)
                    return
                root = root.left
    def print_subtree(self, root):
        if root.left is None and root.right is None:
            return
        print(root.info)
        if root.left:
            print(root.left.info)
            self.print_subtree(root.left)
        if root.right:
            print(root.right.info)
            self.print_subtree(root.right)
    def print_all_nodes(self):
        root = self.root
        print(self.root.info)
        if root.left:
            self.print_subtree(root.left)
        if root.right:
            self.print_subtree(root.right)


if __name__ == '__main__':
    values = []
    for i in range(0, 5):
        n = random.randint(1, 30)
        values.append(n)
    values = [24, 18, 12, 25, 70, 22]
    tree = BinarySearchTree()

    for value in values:
        tree.insert(value)

    tree.print_all_nodes()
