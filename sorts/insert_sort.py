def insert_sort(arr):

    for i in range(len(arr)): # i = 1
        j = i

        while j > 0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1



    print(arr)


insert_sort([1,3,6,2,7,2,4,5,8,4,0])
