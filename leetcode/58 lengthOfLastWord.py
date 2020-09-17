# Source: https://leetcode.com/problems/length-of-last-word/
# Type: String


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        if len(arr) == 0:
            return 0
        return len(arr[-1])
