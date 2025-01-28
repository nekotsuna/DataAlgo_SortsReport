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

def heapsort_descend(list):
  ret = []
  ret_length = len(list)
  length = len(list)

  for i in range(length - 1, 0, -1):
    heapsort_up_descend(list, i)

  i = 0
  while i < ret_length:
    list[0], list[length - 1] = list[length - 1], list[0]
    min_val = list.pop(length - 1)
    ret.append(min_val)
    length = len(list)

    i = i + 1

    heapsort_down_descend(list, 0)
    

  return ret
    

def heapsort_up_descend(list, child_index):
  parent_index = int((child_index + 1) / 2 - 1)
  if parent_index < 0:
    return


  if list[parent_index] < list[child_index]:
    list[parent_index], list[child_index] = list[child_index], list[parent_index]
    heapsort_down_descend(list, child_index)
  

def heapsort_down_descend(list, parent_index):
  length = len(list)

  child_index_first = int((parent_index + 1) * 2 - 1)
  child_index_last = int((parent_index + 1) * 2)
  if child_index_first >= length:
    return
  elif child_index_last >= length:
    child_index_last = child_index_first

  if list[child_index_first] > list[child_index_last]:
    if list[child_index_first] > list[parent_index]:
      list[child_index_first], list[parent_index] = list[parent_index], list[child_index_first]
      heapsort_down_descend(list, child_index_first)
      
  else:
    if list[child_index_last] > list[parent_index]:
      list[child_index_last], list[parent_index] = list[parent_index], list[child_index_last]
      heapsort_down_descend(list, child_index_last)
