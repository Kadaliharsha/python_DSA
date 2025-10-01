def findPages(nums, m):
    n = len(nums)
    
    if n < m:
        return -1
    
    def dfs(i, students_left):
        if i == n and students_left == 0:
            return 0
        
        if i == n or students_left == 0:
            return float('inf')
        
        cur_sum = 0
        best = float('inf')
        
        for j in range(i, n):
            cur_sum += nums[j]
            next_max = dfs(j + 1, students_left - 1)
            
            best = min(best, max(cur_sum, next_max))
            
        return best
    
    return dfs(0, m)

if __name__ == "__main__":
    n1 = list(map(int, input().split()))
    m1 = int(input())
    print(findPages(n1, m1))