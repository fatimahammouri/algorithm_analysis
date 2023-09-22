class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# source code: https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
def insertLevelOrder(arr, i, n):
    root = None 
    if i < n:
        root = Node(arr[i]) 
        # insert left child 
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
        # insert right child 
        root.right = insertLevelOrder(arr, 2 * i + 2, n)
    return root

# ROOT = insertLevelOrder(SSN, 0, len(SSN))