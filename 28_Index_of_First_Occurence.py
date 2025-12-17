class sol:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in (haystack and needle):
            if haystack is None or needle is None:
                return -1
            if haystack == needle:
                return 0
            needl=len(needle)
            for i in range(len(haystack) - needl + 1):
                if haystack[i:i + needl] == needle:
                    return i
            return -1
