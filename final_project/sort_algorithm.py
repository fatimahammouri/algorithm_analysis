def merge_sort(array):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  right_array = array[mid:]
  left_array = array[:mid]
  left = merge_sort(left_array)
  right = merge_sort(right_array)
  return merge(left, right)

def merge(left, right):
  new_array = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      new_array.append(left[i])
      i += 1
    else:
      new_array.append(right[j])
      j += 1
  new_array.extend(left[i:])
  new_array.extend(right[j:])
  return new_array 

# merge_sort(Date)