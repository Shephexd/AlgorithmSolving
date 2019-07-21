class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for y, row in enumerate(matrix):
            for x, _ in enumerate(row[y:]):
                x = x + y
                # print(x, y)
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
            row[:] = row[::-1]


