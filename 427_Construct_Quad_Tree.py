class sol:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
    
            is_all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        is_all_same = False
                        break
                if not is_all_same:
                    break
            

            if is_all_same:
                return Node(grid[r][c] == 1, True)
            

            half = n // 2
            top_left = dfs(half, r, c)
            top_right = dfs(half, r, c + half)
            bottom_left = dfs(half, r + half, c)
            bottom_right = dfs(half, r + half, c + half)
            
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)
            
        return dfs(len(grid), 0, 0)
