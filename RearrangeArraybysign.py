def rearrange(nums):
    n = len(nums)
    
    pos = []
    neg = []
    
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
            
    for i in range(n // 2):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]
        
    return nums

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(rearrange(n))

# The time complexity of this brute force approach is O(n)