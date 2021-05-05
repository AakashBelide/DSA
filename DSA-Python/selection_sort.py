def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

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
        selection_sort(elements)
        print(f'Sorted array: {elements}') 