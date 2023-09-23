from final_objects import TEXT
import time

start = time.time()
def find_pattern(text, pattern):
  indexes = []
  text_length = len(text)
  pattern_length = len(pattern)

  for i in range(0, text_length - pattern_length + 1):
    match = True
    for j in range(pattern_length):
      if text[i+j] != pattern[j]:
        match = False
        break
    if match:
      indexes.append(i)
  return indexes


find_pattern(TEXT, "II")

end = time.time()
print(f"total time: {str(end - start)}") 