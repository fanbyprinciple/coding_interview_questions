# Source: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56#problem
# Time Complexity: O(nlogn)
# Can be improved to O(n) using count sort as the length of array is fixed and can be upto 1000.

def allocation(prices, budget):
    prices.sort()
    houses = 0
    for price in prices:
        if price <= budget:
            houses += 1
            budget -= price
        else: 
            break
    return houses

def inputFunction():
    numTestCase = int(input())
    for i in range(numTestCase):
        N, B = map(int, input().split())
        arr = list(map(int, input().split()))
        print("Case #" + str(i+1) + ": " + str(allocation(arr, B)))

inputFunction()
