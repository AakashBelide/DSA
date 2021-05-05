def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

if __name__ == "__main__":
    tests = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [25, 22, -1, 21, 10, 0],
        [1, 2, 3, 4, 5],
        [9, 8, 7, 2],
        [3],
        []
    ]

    for elements in tests:
        merge_sort(elements)
        print(f'Sorted array: {elements}')