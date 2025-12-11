class sol:
  def best_time(self, nums:List[int]) -> int:
    l,r = 0,1
    maxp = 0
    while r<len(nums):
      if nums[l]<nums[r]:
        maxp = max(maxp, nums[r]-nums[l])
      else:
        l=r
      r+=1
    return maxp
