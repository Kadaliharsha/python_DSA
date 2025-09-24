# Merge two sorted arrays without a third array

# Brute force approach
# So how do I explain the brute force to an interviewer
# The brute force approach involves merging the two arrays into a new array and then sorting the new array.
# This is not efficient, especially for large arrays, as it requires additional space and time for sorting.
# The interviewer asks what is the time complexity and space complexity of this approach.
# The time complexity is O((m+n) log(m+n)) due to the sorting step, and the space complexity is O(m+n) for the merged array.
# So how do we improve upon this?

# Optimal approach 1
# The optimal approach involves using a two-pointer technique to merge the two arrays in place.
# We start with pointers at the end of each array and compare elements, swapping them if necessary.
# This way, we avoid the need for extra space and achieve a time complexity of O(m + n).

def sortedarray(arr1, m, arr2, n):
    # arr1 = [-5 -2 4 5]
    # arr2 = [-3 1 8]
    left = m - 1 # Pointer for the end of arr1's valid elements --> [-5 -2 4 5]
    right = 0 # Pointer for the start of arr2's valid elements --> [-3 1 8]

    while left >= 0 and right < n: # While there are elements to compare --> [-5 -2 4 5] [-3 1 8]
        if arr1[left] > arr2[right]: # Compare elements from both arrays --> 5 > -3 --> True
            arr1[left], arr2[right] = arr2[right], arr1[left] # --> Swap elements --> -3

            left -= 1 # decrement --> 4
            right += 1 # increment --> 1
            
    arr1[:m] = sorted(arr1[:m]) # sorting the elements in arr1

    arr2.sort() # sorting the elements in arr2


    for i in range(m, m + n): # Copying elements from arr2 to arr1 --> 4 to 8
        arr1[i] = arr2[i - m] # explain the step with the example here step by step
        

    return arr1

# def sortedarray(arr1, m, arr2, n):
#     merged = [0] * (m + n)
#     index = 0
#     left = 0
#     right = 0
    
#     while left < m and right < n:
#         if arr1[left] <= arr2[right]:
#             merged[index] = arr1[left]
#             left += 1
#         else:
#             merged[index] = arr2[right]
#             right += 1
#         index += 1
        
#     while left < m:
#         merged[index] = arr1[left]
#         left += 1
#         index += 1
        
#     while right < n:
#         merged[index] = arr2[right]
#         right += 1
#         index += 1
        
#     for i in range(m + n):
#         arr1[i] = merged[i]
    
#     return arr1

if __name__ == "__main__":
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    a = len(nums1)
    b = len(nums2)
    nums1.extend([0] * b)
    print(sortedarray(nums1, a, nums2, b))