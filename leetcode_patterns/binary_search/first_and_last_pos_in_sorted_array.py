from typing import  List

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.search(nums, target, True)
        print(f"start = {start}")
        end = self.search(nums, target, False)
        print(f"end = {end}")
        return [start, end]

    def search(self, nums: List[int], target: int, search_in_left: bool):
        l = 0
        r = len(nums) - 1 # 5
        result = -1
        # [5, 7, 7, 8, 8, 10]
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                if search_in_left:
                    r = mid - 1
                else:
                    l = mid + 1
                result = mid
                continue

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return result


print(Solution().searchRange([5,7,7,8,8,10],8))