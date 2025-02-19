import math

class Solution:
    # Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):

        s_list = list(s)
        n = len(s)

        def permute(start, k_left):
            nonlocal max_till_now, s_list
            cur_max = "".join(s_list)
            if start >= n or k_left == 0:
                return cur_max

            max_digit = max(s_list[start:])

            if s_list[start] != max_digit:
                for i in range(start + 1, n):
                    if s_list[i] == max_digit:
                        s_list[start], s_list[i] = s_list[i], s_list[start]
                        cur_max = max(cur_max, permute(start + 1, k_left - 1))
                        s_list[i], s_list[start] = s_list[start], s_list[i]

            cur_max = max(cur_max,permute(start + 1, k_left))
            return cur_max

        return permute(  0, k)

print(Solution().findMaximumNum("4551711527", 3))
