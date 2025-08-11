def twosum(nums, target):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

if __name__ == "__main__":
    n = list(map(int, input().split()))
    target = int(input())
    print(twosum(n, target))