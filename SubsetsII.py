# Subsets II without duplicates

def subsets(nums):
    res = []
    nums.sort()
    
    def backtrack(start, path):
        res.append(path[:])
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
    backtrack(0, [])
    return res

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(subsets(n))