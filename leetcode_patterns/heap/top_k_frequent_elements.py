from collections import defaultdict
from email.policy import default
from heapq import heappush
from typing import List, Dict
import heapq


class Element:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __repr__(self):
        return f"v{self.val},f{self.freq}"


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq_map :Dict = defaultdict(int)

    for num in nums:
        freq_map[num] += 1
    heap = []

    for item in freq_map.items():
        heap.append(item[0],-item[1])

    heapq.heapify(heap)

    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[0])

    return result

print(topKFrequent([3,0,1,0], k = 1))
