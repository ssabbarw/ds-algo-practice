from collections import defaultdict
from typing import List, NamedTuple


# TODO, Notes: Remember there will be only one element that can occer more than n/2 times
def majorityElement(nums: List[int]) -> int:
    n = len(nums)
    m = defaultdict(int)

    for num in nums:
        m[num] += 1

    n = n // 2
    for key, value in m.items():
        if value > n:
            return key

    return 0

print(majorityElement([2,2,1,1,1,1,1,2,2,2]))