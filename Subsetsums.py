# Subset sums

def subsetsums(nums):
    res = []
    
    def backtrack(i, cur_sum):
        if i == len(nums):
            res.append(cur_sum)
            return 
        
        # Include
        backtrack(i + 1, cur_sum + nums[i])
        
        # exclude
        backtrack(i + 1, cur_sum)
        
    backtrack(0, 0)
    return res

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(subsetsums(n))
    
    
# How do I explain this code in an interview?
# In an interview, you can explain the code step-by-step as follows:
# 1. **Initialization**: Start by defining a function 'subsetsums' that takes a list of integers 'nums' as input. Initialize an empty list 'res' to store the subset sums.
# 2. **Backtracking Function**: Define a nested function 'backtrack' that takes two parameters: the current index 'i' and the current sum 'cur_sum'. This function will be responsible for exploring all possible subsets of the input list.
# 3. **Base Case**: In the 'backtrack' function, check if the current index 'i' is equal to the length of 'nums'. If it is, append the current sum 'cur_sum' to the result list 'res' and return. This indicates that we have considered all elements in the list.
# 4. **Recursive Cases**: If we haven't reached the end of the list, we have two choices for each element:
#    - **Include the current element**: Call 'backtrack' with the next index (i + 1) and add the current element 'nums[i]' to 'cur_sum'.
#    - **Exclude the current element**: Call 'backtrack' with the next index (i + 1) without adding anything to 'cur_sum'.
# 5. **Initial Call**: Start the backtracking process by calling 'backtrack(0, 0)', which begins at the first index with an initial sum of 0.
# 6. **Return Result**: Finally, return the list 'res' containing all possible subset sums.
# You can also discuss the time complexity of the algorithm, which is O(2^n) where n is the number of elements in the input list. This is because each element can either be included or excluded, leading to 2^n possible subsets.
# The space complexity is O(n) for the recursion stack in the worst case.
# You can also mention edge cases, such as when the input list is empty, in which case the only subset sum is 0.
# Example Input/Output:
# Input: 1 2 3
# Output: [0, 1, 2, 3, 3, 4, 5, 6]
# Explanation: The possible subsets are [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] and their sums are 0, 1, 2, 3, 3, 4, 5, 6 respectively.
# What questions can I expect on this code in an interview and give me answers?
# In an interview, you might be asked the following questions about this code:
# 1. **What is the time complexity of this algorithm?**
#    - The time complexity of this algorithm is O(2^n) where n is the number of elements in the input list. This is because each element can either be included or excluded, leading to 2^n possible subsets.
# 2. **What is the space complexity of this algorithm?**
#    - The space complexity is O(n) for the recursion stack in the worst case, where n is the number of elements in the input list. The result list 'res' can also take up to O(2^n) space in the worst case, as it stores all possible subset sums.
# 3. **Can this algorithm handle negative numbers in the input list?**
#    - Yes, this algorithm can handle negative numbers. The subset sums will include all possible combinations of the input numbers, regardless of their sign.
# 4. **What happens if the input list is empty?**
#    - If the input list is empty, the only subset is the empty set, and the only subset sum is 0. The output will be [0].
# 5. **How would you modify the code to return unique subset sums if the input list contains duplicates?**
#    - To return unique subset sums when the input list contains duplicates, you can use a set to store the sums instead of a list. This way, duplicate sums will be automatically handled. You can convert the set back to a list before returning it.
# 6. **Can you explain the backtracking approach used in this code?**
#    - The backtracking approach involves exploring all possible combinations of elements in the input list to find all subset sums. The 'backtrack' function is called recursively with two choices for each element: include it in the current subset or exclude it. This creates a tree of possibilities, and the base case is when all elements have been considered. The current sum is then added to the result list.