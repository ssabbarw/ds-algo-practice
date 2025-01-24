import math
import string
from collections import Counter
from typing import Dict


def minWindow( s: str, t: str) -> str:
    print(len(s))
    if s is None or t is None:
        return ''
    if len(s) < len(t):
        return ''

    min_length_till_now = math.inf
    min_valid_string_till_now = ""
    # bbaa aba
    # b - 1, a = 0
    for start in range(len(s)):
        for end in range(start + len(t), len(s) + 1):
            # print("string = ", s[start:end])
            count_map = Counter(s[start:end])
            is_valid = True
            for char in t:
                if char not in count_map or count_map[char] <= 0:
                    # print(f"countmap = {count_map}")
                    is_valid = False
                    break
                else:
                    count_map[char] -= 1

            if is_valid and end - start + 1 < min_length_till_now:
                min_length_till_now = end - start + 1
                min_valid_string_till_now = s[start:end]

    return min_valid_string_till_now

def minWindowOpt(s: str, t: str) -> str:
    if s is None or t is None:
        return ''
    if len(s) < len(t):
        return ''

    start = 0
    end = start + len(t)
    print(end)
    s_len = len(s)
    min_length = math.inf
    min_sub_string = ""

    while end < s_len + 1:
        sub_string = s[start:end]
        count_map = Counter(sub_string)
        if is_valid(t, count_map):
            if min_length > end - start + 1:
                min_sub_string = sub_string
                min_length = end - start + 1
            start += 1
        else:
            end += 1

    return min_sub_string

def is_valid(t, count_map) -> bool:
    for char in t:
        if count_map[char] > 0:
            count_map[char] -= 1
        else:
            return False
    return True

print(minWindowOpt("bbaa", "aba"))