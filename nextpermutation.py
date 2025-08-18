def nextPermutation(nums):

    # calculate length of the nums
    n = len(nums)
    
    # Step 1 : We find the pivot element
    # So I scan from right to left and find the first pivot
    pivot = n -2
    while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
        pivot -= 1
        
    if pivot >= 0:
        # time to find the successor
        successor = n - 1
        # we need to find the rightmost element which is greater than the pivot
        while nums[successor] <= nums[pivot]:
            successor -= 1
            
        # if successor is found we swap
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        
        
    # now we reverse the suffix
    nums[pivot+1:] = reversed(nums[pivot+1:])
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    nextPermutation(arr)
    print(arr)