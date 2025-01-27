def selectsort_ascend(list):
  length = len(list)

  for i in range(length):
    min_val = list[i]
    min_index = i
    for j in range(i + 1, length):
      if list[j] < min_val:
        min_val = list[j]
        min_index = j

    list[i], list[min_index] = list[min_index], list[i]

  return list

def selectsort_descend(list):
  length = len(list)

  for i in range(length):
    max_val = list[i]
    max_index = i
    for j in range(i + 1, length):
      if list[j] > max_val:
        max_val = list[j]
        max_index = j

    list[i], list[max_index] = list[max_index], list[i]

  return list
