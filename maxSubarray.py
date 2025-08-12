def maxSubarray(nums):
    
    # Brute force approach 
    # Time complexity is O(n ^ 3) 
    # Space complexity is O(1)
    n = len(nums)
    max_sum = float('-inf')
    
    for i in range(n):   # --- O(n)
        for j in range(i, n): # --- O(n)
            sum = 0
            for k in range(i, j + 1): # --- O(n)
                sum += nums[k] 
            max_sum = max(max_sum, sum)      
    return max_sum

    # Better Approach
    # Time complexity is O(n^2)
    # Space complexity is O(1)
    n = len(nums)
    max_len = float('-inf')
    for i in range(n):   # ---- O(n)
        sum = 0
        for j in range(i, n): # ---- O(n)
            sum += nums[j]
            max_len = max(max_len,sum)
    return max_len
    
    # Optimized Approach
    # Time complexity is O(n)
    # Space complexity is O(1)
    n = len(nums)
    max_len = float('-inf')
    cur_sum = 0
    for i in range(n):
        cur_sum += nums[i]
        max_len = max(max_len, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_len

if __name__ == "__main__":
    s = list(map(int, input().split()))
    print(maxSubarray(s))