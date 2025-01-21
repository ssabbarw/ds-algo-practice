def firstBadVersion( n: int) -> int:
    start = 1
    end = n
    prev_bad_index = None

    while start <= end:
        mid = (start + end) // 2

        if isBadVersion(mid):
            prev_bad_index = mid
            end = mid - 1
        else:
            start = mid + 1
    return prev_bad_index

def isBadVersion(version: int) -> bool:
    if version >= 76:
        return True

    return False

print(firstBadVersion(100))