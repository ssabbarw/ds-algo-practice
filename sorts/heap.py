def build_max_heap(arr):
    for i in range(len(arr)//2-1,-1,-1):
        max_heapify(arr,i, len(arr))


def build_min_heap(arr):
    for i in range(len(arr)//2-1,-1,-1):
        min_heapify(arr,i, len(arr))


def max_heapify(arr, i, length):
    largest = i
    left = i*2+1
    right = i*2+2

    if left < length and arr[largest] < arr[left]:
        largest = left

    if right < length and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,largest,length)


def min_heapify(arr, i, length):
    smallest = i
    left = i*2+1
    right = i*2+2

    if left < length and arr[smallest] > arr[left]:
        smallest = left

    if right < length and arr[smallest] > arr[right]:
        smallest = right

    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        min_heapify(arr,smallest,length)





# arr1 = [10,20,30,25,5,40,35,1]
arr1 = [10,35,25,11]

def heap_sort(arr):
    build_min_heap(arr)
    max_index = len(arr) - 1

    for i in range(max_index,0,-1):
        arr[i], arr[0] = arr[0],arr[i]
        min_heapify(arr,0, i)
        pass


heap_sort(arr1)
print(arr1)