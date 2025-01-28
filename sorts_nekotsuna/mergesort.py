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

def mergesort_descend(list):
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

  left = mergesort_descend(left)
  right = mergesort_descend(right)

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
    elif left[left_index] < right[right_index]:
      ret.append(right[right_index])
      right_index = right_index + 1
    elif left[left_index] > right[right_index]:
      ret.append(left[left_index])
      left_index = left_index + 1
    else:
      print(error)

  return ret
