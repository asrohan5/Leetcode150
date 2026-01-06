class sol:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix) , len(matrix[0])
        rz = False
        
        for ro in range(r):
            for co in range(c):
                if matrix[ro][co] == 0:
                    matrix[0][co] = 0
                    
                    if ro>0:
                        matrix[ro][0] = 0
                    else:
                        rz = True
        for ro in range(1,r):
            for co in range(1,c):
                if matrix[0][co] == 0 or matrix[ro][0] == 0:
                    matrix[ro][co] = 0
        
        if matrix[0][0] == 0:
            for ro in range(r):
                matrix[ro][0] = 0
        if rz:
            for co in range(c):
                matrix[0][co] = 0
                    
                        
                    
                
