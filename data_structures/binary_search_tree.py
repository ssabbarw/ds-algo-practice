class BinarySearchTree:
    def __init__(self,key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.key}"

    def insert(self,key):

        if self.key < key:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BinarySearchTree(key=key)
        else:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BinarySearchTree(key=key)

    def inorder(self):
        values = []
        self.__inorder_recursive(values)
        return values

    def __inorder_recursive(self, values):

        if self.left:
            self.left.__inorder_recursive(values)

        values.append(self.key)

        if self.right:
            self.right.__inorder_recursive(values)

    def preorder(self):
        values = []
        self.__preorder_recursive(values)
        return values

    def __preorder_recursive(self,values):
        values.append(self.key)

        if self.left:
            self.left.__preorder_recursive(values)

        if self.right:
            self.right.__preorder_recursive(values)

    def postorder(self):
        values = []
        self.__postorder_recursive(values)
        return values

    def __postorder_recursive(self,values):

        if self.left:
            self.left.__postorder_recursive(values)

        if self.right:
            self.right.__postorder_recursive(values)

        values.append(self.key)

    def search(self, key):
        if key == self.key:
            return self

        if key <= self.key:
            if self.left:
                return self.left.search(key)
            else:
                return None

        if key > self.key:
            if self.right:
                return self.right.search(key)
            else:
                return None

    def delete(self,key):
        current_node = self.search(key)
        if not current_node:
            return

        parent = self.get_parent(current_node)

        new_current_node = None

        if current_node.left:
            new_current_node = current_node.left
        else:
            new_current_node = current_node.right

        if parent.left == current_node:
            parent.left = new_current_node
        else:
            parent.right = new_current_node

        if new_current_node == current_node.left and current_node.right:
            new_current_node_right_most = new_current_node.right_most()
            new_current_node_right_most.right = current_node.right

        current_node.left = None
        current_node.right = None
        current_node = None

    def right_most(self):
        if self.right:
            return self.right.right_most()

        return self

    def get_parent(self, child):
        # if not child is BinarySearchTree:
        #     raise ValueError("Expected a tree node")

        if self.left == child or self.right == child:
            return self

        if self.key <= child.key:
            if self.left:
                return self.left.get_parent(child)
            else:
                return None

        if self.key > child.key:
            if self.right:
                return self.right.get_parent(child)
            else:
                return None

    def inorder_iterative(self):
        stack = []
        inorder_values = []
        current_node = self
        stack.append(current_node)

        while stack:
            while current_node.left:
                current_node = current_node.left
                stack.append(current_node)

            current_node = stack.pop()
            inorder_values.append(current_node.key)

            if current_node.right:
                current_node = current_node.right
                stack.append(current_node)

        return inorder_values

    def inorder_successor(self, node_value):
        """
        :param node:
        :return:inorder successor of given node
        """
        stack = []
        node = self.search(node_value)
        current_node = self
        successor = None
        stack.append(current_node)

        while stack:
            while current_node.left:
                current_node = current_node.left
                stack.append(current_node)


            current_node = stack.pop()

            if current_node == node:
                return successor
            else:
                successor = current_node

            if current_node.right:
                current_node = current_node.right
                stack.append(current_node)

        return None


    def preorder_iterative(self):
        stack = []
        preorder_values = []
        current_node = self
        stack.append(current_node)

        while stack:
            while current_node:
                preorder_values.append(current_node.key)
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()

            current_node = current_node.right


        return preorder_values

    def postorder_iterative(self):
        stack1 = []
        stack2 = []

        stack1.append(self)
        while stack1:
            current_node = stack1.pop()
            stack2.append(current_node.key)

            if current_node.left:
                stack1.append(current_node.left)

            if current_node.right:
                stack1.append(current_node.right)

        return stack2[::-1]

    def postorder_iterative_one_stack(self):
        current_node = self

        post_order_vals = []
        stack = []
        prev = None

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                prev = current_node
                current_node = current_node.left

            current_node = stack[-1]

            if current_node.right and current_node.right != prev:
                current_node = current_node.right
            else:
                # means either have already processed current_node.right or there is no current_node.right
                # so it's time to process the current node
                post_order_vals.append(current_node.key)
                prev = current_node
                stack.pop()
                current_node = None

        return  post_order_vals










# --------------------------------------------------------------------------------------------------------------
root = BinarySearchTree(8)
root.insert(6)
root.insert(15)
root.insert(5)
root.insert(7)
root.insert(11)
root.insert(9)
root.insert(13)
root.insert(18)
root.insert(16)
root.insert(17)
root.insert(10)
root.insert(12)
root.insert(14)

post_order_values = root.postorder()
print(f"postorder = {post_order_values}")

print(root.search(10))
print(root.search(8))
print(root.search(7))
print(root.search(-1))

in_order_values = root.inorder()
print(f"inorder before delete= {in_order_values}")
root.delete(15)

in_order_values = root.inorder()
print(f"inorder after delete = {in_order_values}")
in_order_values = root.inorder_iterative()
print(f"inorder iteratively = {in_order_values}")

successor = root.inorder_successor(15)
print(f"inorder successor of node 15 is = {successor}")


# root.insert(15)
successor = root.inorder_successor(8)
print(f"inorder successor of node 8 is = {successor}")

successor = root.inorder_successor(6)
print(f"inorder successor of node 6 is = {successor}")

successor = root.inorder_successor(14)
print(f"inorder successor of node 14 is = {successor}")

successor = root.inorder_successor(17)
print(f"inorder successor of node 17 is = {successor}")

in_order_values = root.inorder_successor(11)
print(f"inorder successor of node 11 is = {in_order_values}")


pre_order_values = root.preorder()
print(f"preorder = {pre_order_values}")

pre_order_values = root.preorder_iterative()
print(f"preorder iterative = {pre_order_values}")


post_order_values = root.postorder()
print(f"preorder = {post_order_values}")

post_order_values = root.postorder_iterative()
print(f"postorder iterative = {post_order_values}")

post_order_values = root.postorder_iterative_one_stack()
print(f"postorder iterative one stack= {post_order_values}")


# root.insert_data(100)
# root.print_in_order()
# root.delete_data(100,root)
# root.print_in_order()
# val = int(input("Enter node to be deleted\n"))
# root.delete_data(val,root)
# root.print_in_order()





