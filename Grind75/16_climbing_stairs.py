class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.no_of_ways_iterative(n, dp)

    def no_of_ways(self, n, dp):
        if dp[n] != -1:
            return dp[n]

        if n == 1:
            return 1
        if n == 2:
            return 2

        dp[n - 1] = self.no_of_ways(n - 1, dp)
        dp[n - 2] = self.no_of_ways(n - 2, dp)

        return dp[n - 1] + dp[n - 2]

    def no_of_ways_iterative(self, n, dp):
        prev1 = 1
        prev2 = 2

        for i in range(3,n+1):
            temp = prev2
            prev2 += prev1
            prev1 = temp

        return prev2




print(Solution().climbStairs(4))