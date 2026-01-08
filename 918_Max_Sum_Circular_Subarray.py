import math
class sol:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        totalSum = 0
        currMaxSum = 0
        currMinSum = 0
        maxSum = -math.inf 
        minSum = math.inf  

        for num in nums:
            totalSum += num
            
            currMaxSum = max(currMaxSum + num, num)
            maxSum = max(maxSum, currMaxSum)
    
            currMinSum = min(currMinSum + num, num)
            minSum = min(minSum, currMinSum)
    
        if maxSum < 0:
            return maxSum
        else:
            return max(maxSum, totalSum - minSum)
