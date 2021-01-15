# Source: https://leetcode.com/problems/minimum-cost-for-tickets/solution/
# Type: Dynamic Prograpping
# Space: O(n)
# Time: O(n)


# Top down approach.
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costTravellingDay = [0] * 366
        j = 0
        for i in range(1, len(costTravellingDay)):
            if j == len(days):
                costTravellingDay[-1] = costTravellingDay[i - 1]
                break
            
            if i == days[j]:
                dailyTravel = costTravellingDay[i - 1] + costs[0]
                if i - 7 >= 0:
                    weeklyTravel = costTravellingDay[i-7] + costs[1]
                else:
                    weeklyTravel = costs[1]
                if i - 30 >= 0:
                    monthlyTravel = costTravellingDay[i-30] + costs[2]
                else:
                    monthlyTravel = costs[2]
                costTravellingDay[i] = min(dailyTravel, weeklyTravel, monthlyTravel)
                j += 1
            else:
                costTravellingDay[i] = costTravellingDay[i - 1]
            print(costTravellingDay[i],j)
        return costTravellingDay[-1]
