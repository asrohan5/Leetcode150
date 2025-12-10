class Solution:
  def majority_element(self, nums:List[int]) -> int:
    count = {}
    res, maxc = 0,0
    for n in nums:
      count[n] = 1+count.get(n,0)
      res = n if count[n]>maxc else res
      maxc = max(count[n], maxc)
    return res
