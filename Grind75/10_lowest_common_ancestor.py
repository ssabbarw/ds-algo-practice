# Definition for a binary tree node.
from collections import deque
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add_node(self, val):

        if self.val > val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.add_node(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.add_node(val)

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

def search(node: TreeNode, target):
    if node is None:
        return None

    print(f"node.val = {node.val} and target = {target}")
    if node.val == target:
        return node

    if node.val < target:
        if node.right:
            return search(node.right, target)
        else:
            return None
    else:
        if node.left:
            return search(node.left, target)
        else:
            return None



def lowestCommonAncestor( root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root



tree = TreeNode(6)
tree.add_node(2)
tree.add_node(8)
tree.add_node(0)
tree.add_node(4)
tree.add_node(3)
tree.add_node(5)
tree.add_node(7)
tree.add_node(9)

tree.print_level_order()

print(f"lowestCommonAncestor = {lowestCommonAncestor(tree, TreeNode(3),TreeNode(0))}")
