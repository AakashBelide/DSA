def insertionSort(arr):
    ''' Insertion Sort '''

    for i in range(1 , len(arr)):
        
        key = arr[i]
        prev = i-1

        while prev >= 0 and arr[prev] > key : 
            arr[prev+1] = arr[prev]
            prev -= 1
        
        arr[prev+1] = key

    return arr
def bucketSort(arr):

    ''' Bucket Sort '''

    n = len(arr)
    # create n empty buckets
    buckets = [[] for _ in range(n)]
    
    # changing each of the buckets with nearby elements stored
    for i in range(n):
        index = int(n*arr[i])
        buckets[index].append(arr[i])
    
    # sorted array 
    sorted_array = []
    for bucket in buckets:
        # sorting each of the buckets with insertion sort
        insertionSort(bucket)
        # and storing it to sorted array 
        sorted_array.extend(bucket)
    
    return sorted_array

# Execution
if __name__ == '__main__':
    arr = list(map(int , input('Enter elements with space -> ').split()))
    print(bucketSort(arr))
