class sol:
    def countDigitOne(self, n: int) -> int:
        #234
        res = 0
        pow10 = 1
        while pow10 <= n:
            div = pow10 * 10 #1 * 10
            quo = n//div #23
            rem = n%div #4

            res += quo * pow10 #23 * 1

            if rem >= pow10: #4>1
                res += min(rem - pow10+1,pow10) #mins(4 - 1 +1, 1)
            
            pow10 *= 10 #100
        return res
