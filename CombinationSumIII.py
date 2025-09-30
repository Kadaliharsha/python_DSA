def combination3(k, n):
    res = []
    
    def dfs(start, path, target):
        if len(path) == k and target == 0:
            res.append(path[:])
            return
        
        if len(path) > k or target < 0:
            return
        
        for i in range(start, 10):
            dfs(i + 1, path + [i], target - i)
            
    dfs(1, [], n)
    return res

if __name__ == "__main__":
    k1 = int(input())
    n1 = int(input())
    print(combination3(k1, n1))