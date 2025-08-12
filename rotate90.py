def rotatematrix(matrix):
    
    # Brute force approach
    # Time complexity is O(n ^ 2)
    n = len(matrix)
    ans = [[0] * n for _ in range(n)] # initializing an empty array
    
    for i in range(n): # ---> O(n)
        for j in range(n): # ---> O(n)
            ans[j][n - i - 1] = matrix[i][j]
            
    for i in range(n): # ---> O(n)
        matrix[i] = ans[i]
    return matrix


# Optimized Approach
    
    n = len(matrix)
    
    for i in range(n): # ---> O(n)
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for i in range(n): # ---> O(n)
        matrix[i].reverse()
        
    return matrix

if __name__ == "__main__":
    mat = eval(input())
    print(rotatematrix(mat))

            
            