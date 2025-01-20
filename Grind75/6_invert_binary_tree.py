from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_node(self, val):
        node = TreeNode(val)
        if self.val > node.val:
            if self.right:
                self.right.add_node(node.val)
            else:
                self.right = node
        else:
            if self.left:
                self.left.add_node(node.val)
            else:
                self.left = node

    def __str__(self):
        return f"{self.val},"

    def __repr__(self):
        return f"{self.val}"

    def print_level_order(self):
        queue = deque()

        queue.append(self)
        level_order = []

        while queue:
            current = queue.popleft()
            level_order.append(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        print(level_order)




def invertTree( root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    invertTree(root.left)
    invertTree(root.right)

    root.right, root.left = root.left, root.right

    return root

root = TreeNode(4)
root.add_node(2)
root.add_node(7)
root.add_node(1)
root.add_node(3)
root.add_node(6)
root.add_node(9)

root.print_level_order()

invertTree(root)
root.print_level_order()