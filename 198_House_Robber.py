class sol:
    def getmax(sefl,arr):
        return max(arr)
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        for i in range(2,len(nums)):
            nums[i] = self.getmax(nums[:i-1])+nums[i]
        return max(nums[-1], nums[-2])
        
