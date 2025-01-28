import random

length = 10
arr = [random.randint(0, 10) for _ in range(length)]

print(arr)

for i in range(length):
    for j in range(0, length - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print(arr)
print(arr)

