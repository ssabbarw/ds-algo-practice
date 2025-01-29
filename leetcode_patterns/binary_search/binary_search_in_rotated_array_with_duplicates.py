from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]

            print(f"left: {left}, mid {mid}, right: {right}")

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid]:
                left += 1
                continue

            if nums[left] < nums[mid]:
                # left is the sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # left is the sorted half
                if nums[mid] < target <= nums[right]:
                    # if nums[mid] > target >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

print(Solution().search([1,1,2,4,13,1,1,1,1,1,1,1,1],13))