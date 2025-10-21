def fruits(fruits):
    # brute force approach
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # n = len(fruits)
    # maxLen = 0
    
    # for i in range(n):
    #     s = set()
    #     for j in range(i, n):
    #         s.add(fruits[j])
            
    #         if len(s) <= 2:
    #             maxLen = max(maxLen, j - i + 1)
    #         else:
    #             break
            
    # return maxLen

    # better approach
    # Sliding window
    
    n = len(fruits)
    l, r = 0, 0
    maxLen = 0
    mpp = {}
    
    while r < n:
        mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1
        
        if len(mpp) > 2:
            while len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]
                l += 1
                
        if len(mpp) <= 2:
            length = r - l + 1
            maxLen = max(maxLen, length)
                
        r += 1
            
    return maxLen

if __name__ == "__main__":
    f = list(map(int, input().split()))
    print(fruits(f))
                