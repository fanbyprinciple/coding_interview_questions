# https://leetcode.com/problems/robot-bounded-in-circle/
# Time Comlexity: O(n)

class Solution:
    
    def getVector(self, head, x, y, instruction):
        if instruction == 'G':
            if head == 'N':
                y += 1
            elif head == 'S':
                y -= 1
            elif head == 'E':
                x += 1
            else:
                x -= 1
        elif instruction == 'L':
            if head == 'N':
                head = 'W'
            elif head == 'W':
                head = 'S'
            elif head == 'S':
                head = 'E'
            else:
                head = 'N'
        else:
            if head == 'N':
                head = 'E'
            elif head == 'E':
                head = 'S'
            elif head == 'S':
                head = 'W'
            else:
                head = 'N'
        return head, x, y
    
    def isRobotBounded(self, instructions: str) -> bool:
        head = 'N'
        x, y = 0, 0
        for instruction in instructions:
            head, x, y = self.getVector(head, x, y, instruction)
        if (x == 0 and y == 0) or head != 'N':
            return True
        return False
