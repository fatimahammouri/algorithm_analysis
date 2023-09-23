# Build final data objects, used to apply Algorithms  
from data_objects import  SSN, NAMES, DATES

# Helper function to build tree structure from array
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

# ROOT node will be imported and used in Tree Traversal Algorithm 
ROOT = insertLevelOrder(SSN, 0, len(SSN))

# TEXT will be imported and used in pattern matching Brute Force Algorithm
TEXT = "".join(NAMES) 

# YEARS list will be used in Binary Search and Merge Sort Algorithms
YEARS = [int(year[:4]) for year in DATES]
SORTED_YEARS = sorted(YEARS)
print(len(YEARS), len(NAMES), ROOT.data)