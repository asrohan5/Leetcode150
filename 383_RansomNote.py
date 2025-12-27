from collections import Counter
class sol:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = Counter(magazine)
        for n in ransomNote:
            count1[n]-=1
            if count1[n]<0:
                return False
        return True
