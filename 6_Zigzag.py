class sol:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        k = 0
        direction = -1 

        for char in s:
            rows[k] += char
            if k == 0 or k == numRows - 1:
                direction *= -1 
            k += direction

        return "".join(rows)
