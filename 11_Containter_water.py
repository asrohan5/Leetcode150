class sol:
  def container(self, h:List[int]) -> int:
    l,r = 0, len(h)-1
    maxp = 0
    while l<r:
      area = (r-l) * min(h[l], h[r])
      maxp = max(maxp, area)
      if h[l]<h[r]:
        l+=1
      else:
        r-=1
    return maxp
