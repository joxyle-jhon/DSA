class NodeTree:
    def __init__(self, value):
        self.left = None
        self.right = None  
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = NodeTree(value)
            else:
                self.left.insert(value)
        else: 
            if self.right is None:
                self.right = NodeTree(value)  
            else:
                self.right.insert(value)
  

    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.value)
        if self.right:
            self.right.inorderTraversal()

tree = NodeTree(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(5)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

tree.inorderTraversal()
