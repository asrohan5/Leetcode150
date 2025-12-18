class sol:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        pc = [0] * (n+1)

        for c in citations:
            pc[min(c, n)] +=1
        
        h = n
        papers = pc[n]

        while papers <h:
            h-=1
            papers += pc[h]

        return h
