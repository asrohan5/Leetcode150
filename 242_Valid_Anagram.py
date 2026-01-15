class sol:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        import collections
        c = collections.Counter(list(s))
        d = collections.Counter(list(t))
        
        if c==d:
            return True
        return False
