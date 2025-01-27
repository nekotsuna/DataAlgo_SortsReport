def quicksort_ascend(list):
  length = len(list)
  if length <= 1:
    return list

  pivot = list[0]
  left = []
  right = []
  center = [pivot]

  for i in range(1, length):
    if list[i] < pivot:
      left.append(list[i])
    elif list[i] > pivot:
      right.append(list[i])
    else:
      center.append(list[i])

  left = quicksort_ascend(left)
  right = quicksort_ascend(right)

  return left + center + right

def quicksort_descend(list):
  length = len(list)
  if length <= 1:
    return list

  pivot = list[0]
  left = []
  right = []
  center = [pivot]

  for i in range(1, length):
    if list[i] > pivot:
      left.append(list[i])
    elif list[i] < pivot:
      right.append(list[i])
    else:
      center.append(list[i])

  left = quicksort_descend(left)
  right = quicksort_descend(right)

  return left + center + right
