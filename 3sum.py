def threesum(arr):
    n = len(arr)
    
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         for k in range(j + 1, n):
    #             if arr[i] + arr[j] + arr[k] == 0:
    #                 return [arr[i], arr[j], arr[k]]
    # return []

    char_set = set()
    arr.sort()
    
    for i in range(n):
        seen = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in seen:
                char_set.add((arr[i], arr[j], third))
                
            seen.add(arr[j])
    return list(char_set)

    # dry run example [2,-2,0,3,-3,5]
    


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(threesum(nums))
    