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

if __name__ == "__main__":
    s = list(map(int, input().split()))
    print(maxSubarray(s))