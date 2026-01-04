class sol:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        L = len(word)
        visited = [[False for j in range(n)] for i in range(m)]
        
        def DFS(i, j, w):
            if 0 <= i < m and 0 <= j < n and not visited[i][j]:
                w = w + board[i][j]
                visited[i][j] = True
                
                if w == word: return True

                if len(w) == L or not word.startswith(w):
                    visited[i][j] = False
                    return False

                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if DFS(i + x, j + y, w): return True
                
                visited[i][j] = False
        
        for i in range(m):
            for j in range(n):
                if DFS(i, j, ''): return True
        
        return False
