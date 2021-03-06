# Source: https://leetcode.com/problems/fizz-buzz/solution/
# Type: String
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1, n+1):
            if i % 15 == 0:
                a.append("FizzBuzz")
            elif i % 3 == 0:
                a.append("Fizz")
            elif i % 5 == 0:
                a.append("Buzz")
            else:
                a.append(str(i))
        return a
