# Subset sums

def subsetsums(nums):
    res = []
    
    def backtrack(i, cur_sum):
        if i == len(nums):
            res.append(cur_sum)
            return 
        
        # Include
        backtrack(i + 1, cur_sum + nums[i])
        
        # exclude
        backtrack(i + 1, cur_sum)
        
    backtrack(0, 0)
    return res

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(subsetsums(n))