import random

length = 10
arr = [random.randint(0, 10) for _ in range(length)]


def merge(arr):

    length = len(arr)

    if length == 1:
        return arr

    left = arr[:length // 2]
    right = arr[length // 2:]

    left = merge(left)
    right = merge(right)

    new_arr = []
    
    left_i = 0
    right_i = 0

    print(left, right)
    print(len(right), len(left))
    for i in range(length):
        print(i, left_i, right_i, length)
        if right_i >= len(right):
            new_arr.append(left[left_i])
            left_i += 1
        elif left_i >= len(left):
            new_arr.append(right[right_i])
            right_i += 1
        else:
            if left[left_i] < right[right_i]:
                new_arr.append(left[left_i])
                left_i += 1
            else:
                new_arr.append(right[right_i])
                right_i += 1
    print("new", new_arr)

    return new_arr



print(arr)

arr = merge(arr)

print(arr)
