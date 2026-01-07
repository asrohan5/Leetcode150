class sol:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                
                live_neighbors_count = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        if (x, y) != (i, j):
                            live_neighbors_count += board[x][y] & 1

                
                if board[i][j] == 1 and (live_neighbors_count == 2 or live_neighbors_count == 3):
                    board[i][j] |= 0b10  
                elif board[i][j] == 0 and live_neighbors_count == 3:
                    board[i][j] |= 0b10 
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
