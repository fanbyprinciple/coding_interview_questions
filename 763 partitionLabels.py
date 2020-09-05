# Source: https://leetcode.com/problems/partition-labels/
# Type: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i,c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i + 1 - anchor)
                anchor = i + 1
        return ans
