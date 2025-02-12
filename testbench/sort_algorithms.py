def bubblesort_ascend(list):
  length = len(list)

  for i in range(length - 1):
    for j in range(length - 1, i, -1):
      if list[j] < list[j-1]:
        list[j], list[j-1] = list[j-1], list[j]

  return list

def heapsort_ascend(list):
  ret = []
  ret_length = len(list)
  length = len(list)

  for i in range(length - 1, 0, -1):
    heapsort_up_ascend(list, i)

  i = 0
  while i < ret_length:
    list[0], list[length - 1] = list[length - 1], list[0]
    min_val = list.pop(length - 1)
    ret.append(min_val)
    length = len(list)

    i = i + 1

    heapsort_down_ascend(list, 0)
    

  return ret

def heapsort_up_ascend(list, child_index):
  parent_index = int((child_index + 1) / 2 - 1)
  if parent_index < 0:
    return


  if list[parent_index] > list[child_index]:
    list[parent_index], list[child_index] = list[child_index], list[parent_index]
    heapsort_down_ascend(list, child_index)
  

def heapsort_down_ascend(list, parent_index):
  length = len(list)

  child_index_first = int((parent_index + 1) * 2 - 1)
  child_index_last = int((parent_index + 1) * 2)
  if child_index_first >= length:
    return
  elif child_index_last >= length:
    child_index_last = child_index_first

  if list[child_index_first] < list[child_index_last]:
    if list[child_index_first] < list[parent_index]:
      list[child_index_first], list[parent_index] = list[parent_index], list[child_index_first]
      heapsort_down_ascend(list, child_index_first)
      
  else:
    if list[child_index_last] < list[parent_index]:
      list[child_index_last], list[parent_index] = list[parent_index], list[child_index_last]
      heapsort_down_ascend(list, child_index_last)

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

def mergesort_ascend(list):
  if len(list) <= 1:
    return list
   
  ret = []
  left = []
  right = []

  length = len(list)
  half_index = int(length / 2) 
  for i in range(0, length):
    if i < half_index:
      left.append(list[i])
    else:
      right.append(list[i])

  left = mergesort_ascend(left)
  right = mergesort_ascend(right)

  left_index = 0
  left_length = len(left)
  right_index = 0
  right_length = len(right)

  for i in range(len(left) + len(right)):
    if left_index >= left_length: 
      ret.append(right[right_index])
      right_index = right_index + 1
    elif right_index >= right_length:
      ret.append(left[left_index])
      left_index = left_index + 1
    elif left[left_index] > right[right_index]:
      ret.append(right[right_index])
      right_index = right_index + 1
    elif left[left_index] < right[right_index]:
      ret.append(left[left_index])
      left_index = left_index + 1
    else:
      print(error)

  return ret

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
