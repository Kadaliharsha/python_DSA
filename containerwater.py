# container with Most water

def maxArea(height):
    n = len(height)
    left = 0
    right = n - 1
    max_area = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(maxArea(n))
    
# Time complexity: O(n)
# Space complexity: O(1)

# Interview Questions
# 1. What is the brute force approach for this problem?
#    The brute force approach involves checking all possible pairs of lines and calculating the area they can contain. This can be done using nested loops, resulting in a time complexity of O(n^2).

# 2. How can we optimize the solution?
#    We can optimize the solution using the two-pointer technique. By starting with two pointers at the beginning and end of the array, we can calculate the area and then move the pointer pointing to the shorter line inward. This reduces the number of calculations and achieves a time complexity of O(n).

# 3. What is the two-pointer technique?
#    The two-pointer technique involves using two pointers to traverse the array from both ends. In this problem, one pointer starts at the beginning (left) and the other at the end (right). We calculate the area formed by the lines at these pointers and then move the pointer pointing to the shorter line inward, as this could potentially lead to a larger area.

# 4. Can you explain the sliding window concept?
#    The sliding window concept is a technique used to solve problems involving contiguous subarrays or substrings. In this problem, while we are not using a traditional sliding window, the two-pointer approach can be seen as a variation where we adjust the "window" (the area between the two pointers) based on the heights of the lines.

# 5. How do we handle edge cases in this problem?
#    Edge cases include scenarios where the input array is empty or contains only one line. In such cases, the maximum area would be zero since we need at least two lines to form a container. We can handle these cases by checking the length of the input array at the beginning of the function.

# 6. What is the time complexity of the optimized solution?
#    The time complexity of the optimized solution using the two-pointer technique is O(n), where n is the number of lines in the input array.

# 7. What is the space complexity of the optimized solution?
#    The space complexity of the optimized solution is O(1) since we are using a constant amount of extra space.

# 8. Can this problem be solved using dynamic programming?
#    This problem is not typically solved using dynamic programming, as it does not involve overlapping subproblems or optimal substructure. The two-pointer technique is more efficient for this specific problem.

# 9. How would you explain this problem to a non-technical person?
#    Imagine you have a series of vertical lines on a graph, and you want to find the two lines that, when combined with the x-axis, can hold the most water. The goal is to find the maximum area that can be formed between any two lines.

# 10. What are some real-world applications of this problem?
#     This problem can be applied in various fields such as civil engineering (designing containers or
#     reservoirs), computer graphics (calculating bounding boxes), and even in financial modeling (maximizing profit between two points).
# --- IGNORE ---