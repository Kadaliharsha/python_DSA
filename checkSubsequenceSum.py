from functools import lru_cache

def check(nums, k):
    n = len(nums)
    
    @lru_cache(maxsize=None)
    def dfs(i, target):
        # Base case 1:
        if target == 0:
            return True
        
        # Base case 2:
        if i == len(nums):
            return True
        
        if dfs(i + 1, target - nums[i]):
            return True
        
        if dfs(i + 1, target):
            return True
        
        return False
    
    return dfs(0, k)

if __name__ == "__main__":
    nk = list(map(int, input().split()))
    k = int(input())
    print(check(nk, k))