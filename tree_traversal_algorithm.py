from data_objects import  SSN

import time

start = time.time()

def traverse_tree(node):
  if node is None:
    return
  traverse_tree(node.left)
  print(node.value)
  traverse_tree(node.right)

# traverse_tree(root)

end = time.time()
print(f"total time: {str(end - start)}")    