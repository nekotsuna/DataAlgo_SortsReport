def bubblesort_ascend(list):
  length = len(list)

  for i in range(length - 1):
    for j in range(length - 1, i, -1):
      if list[j] < list[j-1]:
        list[j], list[j-1] = list[j-1], list[j]

  return list

def bubblesort_descend(list):
  length = len(list)

  for i in range(length - 1):
    for j in range(length - 1, i, -1):
      if list[j] > list[j-1]:
        list[j], list[j-1] = list[j-1], list[j]

  return list
