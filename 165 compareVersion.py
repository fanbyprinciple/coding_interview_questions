# Source: https://leetcode.com/problems/compare-version-numbers/
# Type: String
# Time Complexity: O(n)

## Can be optimised. No need of 2 for loops!

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        isSwapped = False
        if version2.count(".") < version1.count("."):
            temp = version1
            version1 = version2
            version2 = temp
            isSwapped = True
        
        v1Arr, v2Arr = version1.split("."), version2.split(".")
        for i, s in enumerate(v1Arr):
            if int(s) > int(v2Arr[i]):
                return -1 if isSwapped else 1
            elif int(s) < int(v2Arr[i]):
                return 1 if isSwapped else -1
        
        x = set()
        for i in v2Arr[len(v1Arr):]:
            x.add(int(i))
        if len(v2Arr) > len(v1Arr) and x != {0}:
            return 1 if isSwapped else -1
        return 0
