def combinationSum(n, target):
    result = []
    
    def dfs(i, path, cur_sum):
        if cur_sum == target:
            result.append(path[:])
            return
        
        if cur_sum > target or i == len(n):
            return
        
        dfs(i, path + [n[i]], cur_sum + n[i])
        
        dfs(i + 1, path, cur_sum)
        
    dfs(0, [], 0)
    return result

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = int(input())
    print(combinationSum(A, B))