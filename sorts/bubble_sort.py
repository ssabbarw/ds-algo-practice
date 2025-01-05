def bubble_sort(array):
    for i in range(len(array)):
        did_swap_occur = False
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[i], array[j] = array[j], array[i]
                did_swap_occur = True

        if not did_swap_occur:
            break
    print(f"sorted_array is {array}")

bubble_sort([1,3,6,2,7,2,4,5,8,4,0])



