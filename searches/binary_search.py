def binary_search(sorted_array, left, right, number):

    if left > right:
        return -1

    mid_index = (left + right) // 2

    if sorted_array[mid_index] == number:
        return mid_index
    elif sorted_array[mid_index] > number:
        return binary_search(sorted_array, left, mid_index - 1, number)
    else:
        return binary_search(sorted_array, mid_index + 1, right, number)

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
def binary_search_iterative(sorted_array, left, right, number):

    while left < right:
        mid = (left + right) // 2
        if number == sorted_array[mid]:
            return mid
        elif number > sorted_array[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

for user_input in inputs:
    sorted_arr, low, high, num = user_input
    print(f"Number {num} occurs at index {binary_search(sorted_arr,low,high,num)} in arr{sorted_arr}")
