from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # 6,7,1,2,3,4,5
        min_index = -1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[left]:
                # left half is sorted
                if nums[left] <= target <= nums[mid]:
                    # target is present in left sorted half:
                    right = mid + 1
                else:
                    # target is not present in left sorted half
                    left = mid + 1
            else:
                # right half is sorted
                if nums[right] >= target >= nums[mid]:
                    # target is present in right sorted half:
                    left = mid - 1
                else:
                    # target is not present in right sorted half
                    right = mid - 1

        return -1

    def binary_search(self, nums: List[int], left, right, target):
        print(f"searching in [{nums[left:right + 1]}] with left= {left}., right = {right}")
        # [4,5,6,7,0,1,2]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
                # 1,2,3,4,5,6,7
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


print(Solution().search([6,7,8,1,2,3,4,5], 7))




