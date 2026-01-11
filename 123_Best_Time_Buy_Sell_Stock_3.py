import math
class sol:
    def maxProfit(self, prices: list[int]) -> int:
       
        holdOne = -math.inf  
        sellOne = 0          
        holdTwo = -math.inf 
        sellTwo = 0        
        
        for price in prices:
            sellTwo = max(sellTwo, holdTwo + price)
            holdTwo = max(holdTwo, sellOne - price)
            sellOne = max(sellOne, holdOne + price)
            holdOne = max(holdOne, -price)

        return sellTwo
