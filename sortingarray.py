# Merge two sorted arrays without a third array

# Brute force approach

def sortedarray(arr1, m, arr2, n):
    merged = [0] * (m + n)
    index = 0
    left = 0
    right = 0
    
    while left < m and right < n:
        if arr1[left] <= arr2[right]:
            merged[index] = arr1[left]
            left += 1
        else:
            merged[index] = arr2[right]
            right += 1
        index += 1
        
    while left < m:
        merged[index] = arr1[left]
        left += 1
        index += 1
        
    while right < n:
        merged[index] = arr2[right]
        right += 1
        index += 1
        
    for i in range(m + n):
        arr1[i] = merged[i]
    
    return arr1

if __name__ == "__main__":
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    a = len(nums1)
    b = len(nums2)
    nums1.extend([0] * b)
    print(sortedarray(nums1, a, nums2, b))