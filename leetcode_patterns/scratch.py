class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTreeIterative(inorder, postorder):
    """
    Build a binary tree from inorder and postorder traversal lists using an iterative approach.

    The key idea is to:
    1. Start from the last element of postorder (root)
    2. Keep track of current inorder position
    3. Use a stack to simulate recursion

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not inorder or not postorder:
        return None

    # Create the root node from last element of postorder
    root = TreeNode(postorder[-1])
    stack = [root]

    # Initialize inorder index to last element
    inorder_idx = len(inorder) - 1

    # Process postorder array from right to left
    # Skip the last element as we've already used it for root
    for val in reversed(postorder[:-1]):
        node = TreeNode(val)
        current = stack[-1]

        # Case 1: Current value is right child
        if inorder[inorder_idx] != current.val:
            current.right = node
            stack.append(node)
        # Case 2: Current value is left child of some ancestor
        else:
            # Keep popping until we find the correct parent
            while stack and stack[-1].val == inorder[inorder_idx]:
                current = stack.pop()
                inorder_idx -= 1
            current.left = node
            stack.append(node)

    return root