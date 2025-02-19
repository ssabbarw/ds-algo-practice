import math
from typing import List
import random

def partition(arr,low,high):

    pivot = low
    left = low + 1
    right = high

    while True:
        while left <= high and arr[left] < arr[pivot]:
            left += 1

        while right >= low and arr[right] > arr[pivot] :
            right -= 1

        if left < right and arr[left] > arr[right]:
           arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            break

    return right

def quick_sort(arr, low, high):

    pivot = partition(arr,low,high)

    if abs(low - pivot) > 1:
        quick_sort(arr,low,pivot-1)
    if abs(pivot - high) > 1:
        quick_sort(arr, pivot+1, high)


#         ____________________________________

def quick_sort(nums: List[int])-> List[int]:
    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)

    left = [num for num in nums if num < pivot]
    mid = [num for num in nums if num == pivot]
    right = [num for num in nums if num > pivot]

    return quick_sort(left) + mid + quick_sort(right)

arr1 = [9,8,7,6]
# arr1 = [9,1,3,10,11]
quick_sort(arr1,0,len(arr1)-1)
print(arr1)

