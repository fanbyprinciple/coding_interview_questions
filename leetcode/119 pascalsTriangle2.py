# Source: https://leetcode.com/problems/pascals-triangle-ii/
# Time Complexity: O(n**2)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        currArr = [1]
        for i in range(rowIndex):
            newArr = [1] * (len(currArr) + 1)
            for j in range(1, len(currArr)):
                newArr[j] = currArr[j-1] + currArr[j]
                newArr[-j-1] = newArr[j]
            currArr = newArr
        return currArr 
