class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0  # Counter for the number of inserted elements

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

        self.count += 1  # Increment the counter

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def remove(self, value):
        self.root = self._remove_recursively(self.root, value)
        self.count -= 1  # Decrement the counter

    def _remove_recursively(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._remove_recursively(node.left, value)
        elif value > node.value:
            node.right = self._remove_recursively(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.value = self._find_min_value(node.right)
            node.right = self._remove_recursively(node.right, node.value)
        return node

    def _find_min_value(self, node):
        while node.left:
            node = node.left
        return node.value

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

def main():
    bst = BST()

    while True:
        choice = int(input("BST Operations\n[1] Insertion\n[2] Removal\n[3] Search\n[4] Traversals\n[5] Exit\nEnter your choice: "))

        if choice == 1:
            continue_inserting = True  # Flag to control continuous insertion

            while True:
                if continue_inserting:
                    if bst.count >= 10:
                        print("Maximum input limit (10 nodes) reached.")
                        continue_inserting = False
                    else:
                        value = input("Enter a number to insert or 'done' to stop: ")
                        if value.lower() == "done":
                            if bst.count < 5:
                                print("Minimum input is 5. Please add more nodes.")
                            else:
                                continue_inserting = False
                        else:
                            value = int(value)
                            bst.insert(value)
                            print("----------------------------------------------------------------------")
                            print(f"{value} inserted into the BST. ({bst.count} elements in the BST)")
                            if bst.count >= 10:
                                continue_inserting = False  # Stop inserting after 10 elements
                else:
                    choice = int(input("BST Operations: [1] Insertion [2] Removal [3] Search [4] Traversals [5] Exit\nEnter your choice: "))  # Re-ask for choice to exit insertion mode
                
                if choice == 1:
                    print("You're already in insertion mode. Use 'done' to stop inserting.")
                    print("----------------------------------------------------------------------")

                elif choice == 2:
                    value = int(input("Enter a number to remove: "))
                    if bst.search(value):
                        bst.remove(value)
                        print(f"{value} removed from the BST.")
                    else:
                        print(f"{value} is not present in the BST.")
                elif choice == 3:
                    value = int(input("Enter a number to search for: "))
                    if bst.search(value):
                        print(f"{value} is present in the BST.")
                    else:
                        print(f"{value} is not present in the BST.")
                elif choice == 4:
                    if bst.count >= 5:
                        print("Preorder Traversal:")
                        bst.preorder_traversal(bst.root)
                        print("\nInorder Traversal:")
                        bst.inorder_traversal(bst.root)
                        print("\nPostorder Traversal:")
                        bst.postorder_traversal(bst.root)
                    else:
                        print("Minimum input is 5. Please add more nodes.")
                    print("\n")
                elif choice == 5:
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please enter a valid option (1-5).")
        elif choice == 2:
            value = int(input("Enter a number to remove: "))
            if bst.search(value):
                bst.remove(value)
                print(f"{value} removed from the BST.")
            else:
                print(f"{value} is not present in the BST.")
        elif choice == 3:
            value = int(input("Enter a number to search for: "))
            if bst.search(value):
                print(f"{value} is present in the BST.")
            else:
                print(f"{value} is not present in the BST.")
        elif choice == 4:
            if bst.count >= 5:
                print("----------------------------------------------------------------------")
                print("Preorder Traversal:")
                bst.preorder_traversal(bst.root)
                print("\nInorder Traversal:")
                bst.inorder_traversal(bst.root)
                print("\nPostorder Traversal:")
                bst.postorder_traversal(bst.root)
                print("----------------------------------------------------------------------")
            else:
                print("Minimum input is 5. Please add more nodes.")
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
