def searchX(nums, target):
    n = len(nums)
    
    for i in range(n):
        if nums[i] == target:
            return i
    return - 1

if __name__ == "__main__":
    nick = list(map(int,input().split()))
    xick = int(input())
    print(searchX(nick, xick))