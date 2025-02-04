class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def in_order_traversal(self):
        elements = []
        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # Visit base node
        elements.append(self.data)
        # Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    def pre_order_traversal(self):
        elements = []
        # Visit base node
        elements.append(self.data)
        # Visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        # Visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    def post_order_traversal(self):
        elements = []
        # Visit left tree
        if self.left:
            elements += self.left.post_order_traversal()
        # Visit right tree
        if self.right:
            elements += self.right.post_order_traversal()
        # Visit base node
        elements.append(self.data)
        return elements
    def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i])
        return root
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
        return False
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def delete(self, value):
        if value < self.data:
            if self.left:
                if self.left:
                    self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        return self

def DFS(root: BinarySearchTreeNode) -> list:
    if not root:
        return []
    return [root.data] + DFS(root.left) + DFS(root.right)

if __name__ == "__main__":
    root = BinarySearchTreeNode(1)
    root.add_child(2)
    root.add_child(3)
    root.add_child(4)
    root.add_child(5)
    print(DFS(root)) # [1, 2, 4, 5, 3]