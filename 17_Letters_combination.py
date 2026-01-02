class sol:
    def letterCombinations(self, digits: str) -> List[str]:
        L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        lend = len(digits)
        ans = []
        if digits=="": return []
        def bfs(pos:int, st:str):
            if pos==lend: ans.append(st)
            else:
                letters = L[digits[pos]]
                for letter in letters:
                    bfs(pos+1, st+letter)
        bfs(0,"")
        return ans
