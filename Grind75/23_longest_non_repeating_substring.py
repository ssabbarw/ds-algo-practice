def lengthOfLongestSubstring(s: str) -> int:
    if s is None:
        return 0

    seen = set()
    left = right = 0
    print(len(s))
    max_length  = 0
    while left <= right < len(s):
        print(left, right, s[right], seen)
        if s[right] not in seen:
            seen.add(s[right])
            right += 1
            max_length = max(max_length, len(seen))
        else:
            seen.remove(s[left])
            left = left + 1

    return max_length

print(lengthOfLongestSubstring("1234"))