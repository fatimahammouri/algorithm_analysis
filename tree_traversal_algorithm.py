from final_objects import ROOT
import time

start = time.time()

def traverse_tree(node):
  if node is None:
    return
  traverse_tree(node.left)
  traverse_tree(node.right)

traverse_tree(ROOT)

end = time.time()
print(f"total time: {str(end - start)}")    