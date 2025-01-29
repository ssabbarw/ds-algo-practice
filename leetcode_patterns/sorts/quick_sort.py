from typing import List
import random

def quick_sort(nums: List[int])-> List[int]:
    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)

    left = [num for num in nums if num < pivot]
    mid = [num for num in nums if num == pivot]
    right = [num for num in nums if num > pivot]

    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([3, 2, 1, 5, 6, 4]))
print(quick_sort([]))
print(quick_sort([1]))
print(quick_sort([1,2,3,4,5,6]))
print(quick_sort([6,5,4,3,2,1]))