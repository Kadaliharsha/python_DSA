# Remove duplicates from sorted array

def remove_duplicates(nums):
    nums.sort()
    if not nums:
        return []
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            
    return nums[:i + 1]

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(remove_duplicates(n))
    
