class sol:
    def romanToInt(self, s: str) -> int:
        rom = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        num = rom[s[n-1]]
        for i in range(n-2, -1,-1):
            if rom[s[i]] >= rom[s[i+1]]:
                num+=rom[s[i]]
            else:
                num-=rom[s[i]]
        return num
