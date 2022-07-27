#TC: O(len(costs)*3) = O(n) since no of colors is fixed to 3
#SC: O(1) since we are modifying in the input 2d matrix and returning a number from the matrix

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        for i in range(1,len(costs)):
            costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
            costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
            costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]
            
        return min(costs[-1])