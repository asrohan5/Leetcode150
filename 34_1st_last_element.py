class sol:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binsearch1(nums,target, True)
        right = self.binsearch1(nums,target, False)
        return [left,right]
        
    def binsearch1(self, nums, target, bias):
        l,r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l+r)//2
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
                
            else:
                i=m
                if bias:
                    r = m-1
                else:
                    l = m+1
        return i
            
