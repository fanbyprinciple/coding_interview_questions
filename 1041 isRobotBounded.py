# https://leetcode.com/problems/robot-bounded-in-circle/
# Time Comlexity: O(n)

class Solution:
    
    def getVector(self, head, coord, instruction):
        if instruction == 'G':
            if head == 'N':
                coord[1] += 1
            elif head == 'S':
                coord[1] -= 1
            elif head == 'E':
                coord[0] += 1
            else:
                coord[0] -= 1
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
        return head, coord
    
    def isRobotBounded(self, instructions: str) -> bool:
        head = 'N'
        coord = [0, 0]
        for instruction in instructions:
            head, coord = self.getVector(head, coord, instruction)
        if coord == [0,0] or head != 'N':
            return True
        return False
