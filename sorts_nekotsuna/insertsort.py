def insertsort_ascend(list):
  length = len(list)

  for i in range(1, length):
    insert_val = list.pop(i)
    for j in range(i):
      if insert_val < list[j]:
        list.insert(j, insert_val)
        break
      elif j == i - 1:
        list.insert(i, insert_val)

  return list

def insertsort_descend(list):
  length = len(list)

  for i in range(1, length):
    insert_val = list.pop(i)
    for j in range(i):
      if insert_val > list[j]:
        list.insert(j, insert_val)
        break
      elif j == i - 1:
        list.insert(i, insert_val)

  return list
