def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor

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
        insertion_sort(elements)
        print(f'Sorted array: {elements}')