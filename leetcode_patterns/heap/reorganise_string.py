import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter_map = Counter(s)
        max_heap = [(-item[1], item[0]) for item in counter_map.items()]
        print(counter_map)
        heapq.heapify(max_heap)

        highest_freq = max_heap[0][0]
        print(max_heap[0])

        result = ""

        if len(s) % 2 == 0:
            if -highest_freq > (len(s) // 2):
                return result
        else:
            if -highest_freq > (len(s) // 2) + 1:
                return result

        prev = None
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result += char

            if prev and prev[0]:
                heapq.heappush(max_heap, prev)

            prev = (freq + 1, char)

        return result

print(Solution().reorganizeString("aab"))




