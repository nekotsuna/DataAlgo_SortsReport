import random

length = 10
arr = [random.randint(0, 10) for _ in range(length)]

arr = [2, 4, 1, 5, 6, 3]


def heap(arr):
    build_max_heap(arr)


    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)



def max_heapify(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    print(left, right, largest)

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(arr, largest, n)
        max_heapify(arr, largest, n)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)
        print(arr)
    
print(arr)
heap(arr)

print(arr)
