from typing import  List
def find_rotation_point_in_sorted_array(nums: List[int]):
    left = 0
    right = len(nums) - 1

    if nums[left] < nums[right]:
        return -1

    while left < right:
        mid = (left + right) // 2

        # If mid+1 is the rotation point
        if nums[mid] > nums[mid + 1]:
            return mid + 1, nums[mid + 1]

        # If mid is the rotation point
        if nums[mid - 1] > nums[mid]:
            return mid, nums[mid]

        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1

nums = [8, 9, 10, 11, 12, 13, 14, 4, 5, 6, 7]
print(f"rotation at : {find_rotation_point_in_sorted_array(nums)}")