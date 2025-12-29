class sol:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        top, bot = 0, r-1
        while top<= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row +1
            elif target<matrix[row][0]:
                bot = row -1
            else:
                break
        if not (top <=bot):
            return False
        row = (top+bot)//2
        l,f = 0,c-1
        while l<=f:
            mid = (l+f)//2
            if target > matrix[row][mid]:
                l = mid+1
            elif target < matrix[row][mid]:
                f = mid-1
            else:
                return True
        return False
        
