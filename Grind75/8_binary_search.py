from typing import List


def binary_search_recursive(nums, target, low, high):
    if low > high or low < 0 or high > len(nums):
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return binary_search_recursive(nums, target, 0, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, high)


def binary_search_iterative(nums, target, low, high):
    if low > high or low < 0 or high > len(nums):
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return binary_search_recursive(nums, target, 0, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, high)


def binary_search(nums: List[int], target: int):
    if not nums or nums[-1] < target or nums[0] > target:
        return -1

    return binary_search_recursive(nums, target, low = 0, high = len(nums) - 1)


def binary_search_iterative(nums: List[int], target: int):
    low = 0
    high = len(nums)

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            high = mid -1
        else:
            low = mid + 1

    return -1

print(binary_search_iterative([-1,0,3,5,9,12], 3))