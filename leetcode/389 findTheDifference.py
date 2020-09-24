# Source: https://leetcode.com/problems/find-the-difference/
# Type: Hash Table/Dicts/Array, Bitwise Operations
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # My solution. i used array. A more optimised way will be to use dicts (hash maps). 
        # Will give access in O(1)
        arr = [0] * 26
        for i in range(len(s)):
            arr[ord(t[i]) - ord('a')] += 1
            arr[ord(s[i]) - ord('a')] -= 1
        arr[ord(t[-1]) - ord('a')] += 1
        for i, c in enumerate(arr):
            if c != 0:
                return chr(ord('a') + i)
            
        # Another approach is to use XOR Bitwise operation. 
        # Since XOR of two same number will always return 0.
        # Using it to find the extra character is a smart approach
        
        # ans = 0
        # for c in s + t:
        #     ans ^= ord(c)
        # return chr(ans)
