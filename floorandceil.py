def floorandceil(nums, x):
    floor = -1
    ceil = -1 
    
    for num in nums:
        if num <= x and num > floor:
            floor = num
        if num >= x and (ceil == -1 or num < ceil):
            ceil = num
            
    return [floor, ceil]

if __name__ == "__main__":
    nick = list(map(int, input().split()))
    xick = int(input())
    print(floorandceil(nick, xick))