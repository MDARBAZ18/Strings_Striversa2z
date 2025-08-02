# write a code to set the matrix zeroes
def setmatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zeros = []
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeros.append((i,j))
                
    for i,j in zeros:
        for k in range(rows):
            matrix[i][k]= 0
        for k in range(cols):
            matrix[k][j]= 0
            
    
matrix =[ [1,2,3] ,
         [4,0,6],
         [7,8,9]]
setmatrix(matrix)
print(matrix)
                
## UPPER JO HAIN VO BRUTE FORCE HAI PHATTE THEEK HAI?

# AB OPTIMAL CODE LEKHTU PHAATTE DEKHO 

def setzeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_marker = [False]*rows
    cols_marker = [False]*cols
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_marker[i] = True
                cols_marker[j] = True
    for i in range(rows):
        for j in range(cols):
            if row_marker[i] or cols_marker[j]:
                matrix[i][j] = 0
                
matrix = [[1,2,3],[4,0,6],[7,8,9]]
setzeros(matrix)
print(matrix)


           
                
                