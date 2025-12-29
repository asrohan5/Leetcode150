class sol:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            
            midv = nums[mid]
            tl = nums[mid-1] if mid>0 else float('-inf')
            tr = nums[mid+1] if mid<len(nums)-1 else float('-inf')
            
            if tl < midv > tr:
                return mid
            elif tl<midv<tr:
                l = mid+1
            else:
                r = mid-1
