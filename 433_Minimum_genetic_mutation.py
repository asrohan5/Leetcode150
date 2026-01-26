import collections
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank_set = set(bank)
        

        if endGene not in bank_set:
            return -1
        
        GENES = ['A', 'C', 'G', 'T']
        
        queue = collections.deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            current_gene, steps = queue.popleft()
            
            if current_gene == endGene:
                return steps
            
            for i in range(len(current_gene)):
                for char in GENES:
                
                    neighbor = current_gene[:i] + char + current_gene[i+1:]
    
                    if neighbor in bank_set and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
    
        return -1

