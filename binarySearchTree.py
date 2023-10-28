class NodeTree:
    def __init__(self, value, content = None):
        self.left = None
        self.right = None  
        self.value = value
        self.content = None
    
    def insert(self, value, content = None):
        if value < self.value:
            if self.left is None:
                self.left = NodeTree(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else: 
            if self.right is None:
                self.right = NodeTree(value) 
                self.right.content = content
            else:
                self.right.insert(value, content)
  

    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.value)
        if self.right:
            self.right.inorderTraversal()

    def preorderTraversal(self):
        print(self.value)
        if self.left:
            self.left.preorderTraversal()
        if self.right:
            self.right.preorderTraversal()
    
    def postorderTraversal(self):
        if self.left:
            self.left.postorderTraversal()
        if self.right:
            self.right.postorderTraversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self



tree = NodeTree(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19, {"data": "Hello, World"})
tree.insert(5)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

# tree.inorderTraversal()
# tree.preorderTraversal()
# tree.postorderTraversal()
print(tree.find(19).content['data'])
