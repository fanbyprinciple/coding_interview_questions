# Source: https://leetcode.com/problems/gas-station/
# Type: Greedy
# Time Complexity: O(n)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasAvailable, gasNeeded, start = 0, 0, 0
        
        for i in range(len(gas)):
            gasAvailable += gas[i] - cost[i]
            if gasAvailable < 0:
                start = i + 1
                gasNeeded += gasAvailable
                gasAvailable = 0
        return -1 if gasAvailable + gasNeeded < 0 else start
