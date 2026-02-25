def transpose(matrix):
        
     row = len(matrix)
     column = len(matrix[0])

     transp_matrix = [[0] * row for _ in range(column)]
     for i in range(row):
            for j in range(column):
                transp_matrix[j][i] = matrix[i][j]
     return transp_matrix


test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(test))