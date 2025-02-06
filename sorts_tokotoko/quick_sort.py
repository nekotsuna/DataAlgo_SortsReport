def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    st_num = arr[0]
    left = [x for x in arr[1:] if x <= st_num]
    right = [x for x in arr[1:] if x > st_num]
    return quick_sort(left) + [st_num] + quick_sort(right)
