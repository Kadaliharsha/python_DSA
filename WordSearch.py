# Word Search

def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    
    def backtrack(r, c, k):
        if k == len(word):
            return True
        
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
            return False
        
        temp = board[r][c]
        board[r][c] = "#"
        
        found = (backtrack(r + 1, c, k + 1) or
                 backtrack(r - 1, c, k + 1) or
                 backtrack(r, c + 1, k + 1) or
                 backtrack(r, c - 1, k + 1))
        
        board[r][c] = temp
        return found
    
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False

if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB"
    
    print(exist(board, word1))  # Output: True
    print(exist(board, word2))  # Output: True
    print(exist(board, word3))  # Output: False