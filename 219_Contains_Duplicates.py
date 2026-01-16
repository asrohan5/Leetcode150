class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
      
        for index, value in enumerate(nums):
            if value in index_map and index - index_map[value] <= k:
                return True
            index_map[value] = index
        return False
