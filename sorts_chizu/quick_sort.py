import random

length = 10
arr = [random.randint(0, 10) for _ in range(length)]

def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_idx = len(arr) // 2
    pivot = arr[pivot_idx]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick(left) + middle + right

arr = quick(arr)
print(arr)
