# Source: https://leetcode.com/problems/sort-array-by-parity/
# Topic: Array
# Time Complexity: O(n)

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i]%2 != 0 and A[j]%2 != 1:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                i += 1
                j -= 1
            if A[i]%2 == 0:
                i += 1
            if A[j]%2 == 1:
                j -= 1
        return A
