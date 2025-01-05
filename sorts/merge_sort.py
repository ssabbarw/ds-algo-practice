def merge_sorted_arrays(arr1, arr2):
    arr1_index = 0
    arr2_index = 0
    merged_array = []

    while arr1_index < len(arr1) and arr2_index < len(arr2):
        if arr1[arr1_index] < arr2[arr2_index]:
            merged_array.append(arr1[arr1_index])
            arr1_index += 1
        else:
            merged_array.append(arr2[arr2_index])
            arr2_index += 1

    # for index in range(arr1_index,len(arr1)):
    #     merged_array.append(arr1[index])
    #
    # for index in range(arr2_index,len(arr2)):
    #     merged_array.append(arr2[index])

    merged_array += arr1[arr1_index:]
    merged_array += arr2[arr2_index:]

    return merged_array


def merge_sort(arr):

    if len(arr) == 1:
        return arr
    mid_index = len(arr)//2

    sorted_array = merge_sorted_arrays(merge_sort(arr[:mid_index]), merge_sort(arr[mid_index:]))
    return sorted_array

arr1 = merge_sort([1,3,9,20,22]+[2,3,9,12,13,15])
print(f"Sorted array = {arr1}")



def merge_sorted_arrays_using_recursion(sorted_arr1 ,sorted_arr2, index1=0, index2=0):

    if index1 == len(sorted_arr1):
        return sorted_arr2[index2:]

    if index2 == len(sorted_arr2):
        return sorted_arr1[index1:]

    if sorted_arr1[index1] < sorted_arr2[index2]:
        return [sorted_arr1[index1]] + merge_sorted_arrays_using_recursion(sorted_arr1, sorted_arr2, index1+1, index2)
    else:
        return [sorted_arr2[index2]] + merge_sorted_arrays_using_recursion(sorted_arr1, sorted_arr2, index1, index2+1)


arr1 = merge_sorted_arrays_using_recursion([1,3,9,20,22],[2,3,9,12,13,15])
print(f"Sorted array using recursion= {arr1}")