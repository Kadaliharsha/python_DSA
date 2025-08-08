def leaders(nums):
    n = len(nums)
    arr = []
    
    for i in range(n):
        leader = True
        for j in range(i + 1, n):
            if nums[i] <= nums[j]:
                leader = False
                break
        if leader:
            arr.append(nums[i])
    return arr

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(leaders(n))