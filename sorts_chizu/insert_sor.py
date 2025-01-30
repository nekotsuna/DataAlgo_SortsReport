import random

length = 10
arr = [random.randint(0, 10) for _ in range(length)]

def insert(arr):
    for i in range(1, len(arr)):
        print(arr)
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr_i = arr[i]
                arr[j+1:i+1] = arr[j:i]
                arr[j] = arr_i
                break
    return arr


print(arr)
arr = insert(arr)

print(arr)
