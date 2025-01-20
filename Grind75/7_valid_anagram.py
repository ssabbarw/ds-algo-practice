from typing import Dict
from collections import Counter, defaultdict


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    if s==t:
        return True

    s_map = defaultdict(int)
    t_map = defaultdict(int)

    for char in s:
        s_map[char] += 1

    for char in t:
        t_map[char] += 1

    return s_map == t_map

print(isAnagram("anagram", "armnaga"))
print(Counter("anagram"))