from final_objects import SORTED_YEARS
import time

start = time.time()

def binary_search(array, target):
  low, high = 0, len(array) - 1
  while low <= high:
    mid = (low + high) // 2
    if target == array[mid]:
      return mid
    elif target > array[mid]:
      low = mid + 1
    else:
      high = mid - 1
  return -1

binary_search(SORTED_YEARS, 1990)

end = time.time()
print(f"total time: {str(end - start)}")