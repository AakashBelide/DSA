def swap(a, b, arr):
    if a!= b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end -= 1
        
        if start < end:
            swap(start, end, elements)
    
    swap(pivot_index, end, elements)

    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)

        quick_sort(elements, start, pi-1) # Left partition
        quick_sort(elements, pi+1, end) # Right partition

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
        quick_sort(elements, 0, len(elements)-1)
        print(f'Sorted array: {elements}')