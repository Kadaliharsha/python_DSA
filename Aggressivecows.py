def canPlaceCows(nums, dist, k):
    count = 1
    last = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - last >= dist:
            count += 1
            last = nums[i]
        if count >= k:
            return True
    return False

def aggressivecows(nums, k):
    nums.sort()
    n = len(nums)
    low = 1
    high = nums[n - 1] - nums[0]
    while low <= high:
        mid = (low + high) // 2
        if canPlaceCows(nums, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high

if __name__ == "__main__":
    nik = list(map(int, input().split()))
    kk = int(input())
    print(aggressivecows(nik, kk))
    