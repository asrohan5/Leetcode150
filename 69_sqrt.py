class sol:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        r=x
        while r*r>x:
            r = (r+x//r)//2
        return r

'''
class sol:
    def mySqrt(self, x: int) -> int:
        l,r = 1, x//2
        if x<2:
            return x
        
        while l<=r:
            mid = (l+r)//2
            if mid==x//mid:
                return mid
            elif mid>x//mid:
                r = mid-1
            else:
                l = mid+1
        return r
            
'''
