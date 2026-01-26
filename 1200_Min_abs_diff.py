class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:        
        arr.sort()
        mindiff = float('inf')
        res = []
        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            if mindiff > diff:
                res.clear()
                mindiff = min(diff, mindiff)
            if diff == mindiff:
                res.append([arr[i], arr[i+1]])
            
        return res

