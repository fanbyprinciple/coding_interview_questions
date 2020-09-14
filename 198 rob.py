# Source: https://leetcode.com/problems/house-robber/
# Type: Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

## I really suck at DP. Leetcode has marked it at easy. Is it me or Leetcode needs to change its criterias?

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i - 1])
        return dp[-1]
