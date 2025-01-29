from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k):
            result = heapq.heappop(heap)

        return result




print(Solution().findKthLargest([3,2,1,5,6,4], 2))
