from collections import defaultdict
from email.policy import default


def character_replacement_brute_force(s: str, k: int) -> int:
    print(len(s))
    # Try for each unique character in the string
    return max(max_length_with_char(s, k, char) for char in set(s))

def max_length_with_char(s: str, k :int, char: str) -> int:
    max_length = 0
    for start in range(len(s)):
        replacements_used = 0
        current_length = 0
        for end in range(start, len(s)):
            if char != s[end]:
                if replacements_used < k:
                    replacements_used += 1
                else:
                    break
            current_length += 1

        max_length = max(max_length, current_length)

    return max_length

def character_replacement_with_sliding_window(s: str, k: int) -> int:

    left = 0
    freq_counter = defaultdict(int)
    max_length = 0
    current_max_freq = 0


    for right in range(len(s)):
        freq_counter[s[right]] += 1
        current_max_freq = max(current_max_freq, freq_counter[s[right]])

        if right - left + 1 - current_max_freq > k:
            freq_counter[s[left]] -= 1
            left = left + 1

        max_length = max(max_length, right - left + 1)
    return max_length




    # Try for each unique character in the string
    return max(max_length_with_char(s, k, char) for char in set(s))

print("ans", character_replacement_with_sliding_window("ABAB", 0))