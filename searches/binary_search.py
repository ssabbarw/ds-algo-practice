def binary_search(sorted_arr, low, high, num):

    if low > high:
        return -1

    mid_index = (low + high) // 2

    if sorted_arr[mid_index] == num:
        return mid_index
    elif sorted_arr[mid_index] > num:
        return binary_search(sorted_arr, low, mid_index - 1, num)
    else:
        return binary_search(sorted_arr, mid_index + 1, high, num)

inputs = [
    ([0,1,2,3,4,5,6,7],0,7,6),
    ([0,1,2,3,4,5,6,7],0,7,2),
    ([0,1,2,3,4,5,6,7],0,7,-10),
    ([0,1,2,3,4,5,6,7],0,7,10),
]

print("\nRecursive binary search")
for user_input in inputs:
    sorted_arr, low, high, num = user_input
    print(f"Number {num} occurs at index {binary_search(sorted_arr,low,high,num)} in arr{sorted_arr}")

print("\nIterative binary search")
def binary_search_iterative(sorted_array, low, high, num):

    while True:
        if low > high:
            return -1
        mid = (low + high) // 2
        if num == sorted_array[mid]:
            return mid
        elif num > sorted_array[mid]:
            low = mid + 1
        else:
            high = mid - 1

for user_input in inputs:
    sorted_arr, low, high, num = user_input
    print(f"Number {num} occurs at index {binary_search(sorted_arr,low,high,num)} in arr{sorted_arr}")
