import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_map = collections.defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            anagrams_map[key].append(word)
        
        return list(anagrams_map.values())
