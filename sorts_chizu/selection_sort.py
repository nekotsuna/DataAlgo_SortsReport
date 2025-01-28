import random

length = 10

arr = [random.randint(0, 10) for _ in range(length)]

print(arr)

for i in range(length):
    min_idx = i
    for j in range(i, length):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)

print(arr)



