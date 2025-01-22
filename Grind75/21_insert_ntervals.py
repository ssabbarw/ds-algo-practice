from typing import List

# Better solution
def insert_better(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    new_interval_left_bound = newInterval[0]
    new_interval_right_bound = newInterval[1]
    result = []
    n = len(intervals)

#     add all those intervals to result, which lie before new interval
    i = 0
    while i < n and intervals[i][1] < new_interval_left_bound:
        result.append(intervals[i])
        i += 1


#     now merge all those intervals which overall with new interval(if any)
    while i< n and intervals[i][1] > new_interval_right_bound:
        new_interval_right_bound = max(new_interval_right_bound[1], intervals[i][1])
        new_interval_left_bound = min(new_interval_left_bound, intervals[i][0])
        i += 1

    result.append([new_interval_left_bound, new_interval_right_bound])

    while i < n:
        result.append(intervals[i])
        i += 1

    return result





# my solution
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    intervals.append(newInterval)
    new_intervals = []

    for i in range(len(intervals) - 1, 0, -1):
        if intervals[i][0] < intervals[i - 1][0]:
            intervals[i], intervals[i - 1] = intervals[i - 1], intervals[i]

            # new interval added at apt place, now let's merge overlapping intervals
    print(intervals)
    # Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    for i in range(len(intervals)):
        if i < len(intervals)-1 and intervals[i][0] <= intervals[i + 1][0] <= intervals[i][1]:
            intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
            intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
        else:
            new_intervals.append(intervals[i])

    return new_intervals

print(insert([[1,3],[6,9]], [2,5]))
