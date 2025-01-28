from typing import List
def binary_search(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) //2

        if nums[mid] == target:
            return f"index = {mid},number={nums[mid]}"

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    return "index = -1", None

print(binary_search([1,2,3,4,5,6,7,8,9], 18))
