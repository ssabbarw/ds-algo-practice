from typing import List
import random
import heapq

def findKthLargestWithHeap(self, nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)

    for _ in range(k):
        result = heapq.heappop(heap)

    return result

def findKthLargest(nums: List[int], k: int) -> int:
    if len(nums) == 1:
        return nums[0]

    pivot = nums[-1]

    left = [num for num in nums if num > pivot]  #
    mid = [num for num in nums if num == pivot]  # 6
    right = [num for num in nums if num < pivot]  # 5

    if len(left) >= k:
        return findKthLargest(left, k)

    if len(left) + len(mid) >= k:
        return mid[0]

    return findKthLargest(right, k - len(left) - len(mid))

print(findKthLargest([3,2,1,5,6,4], 2))

