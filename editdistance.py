# Edit distance between two strings

# The function editdistance calculates the minimum number of operations required to convert one string (start) into another string (target). The allowed operations are insertion, deletion, and substitution of a single character.

def editdistance(start, target):
    m = len(start)  # Length of the first string
    n = len(target) # Length of the second string
    
    # Create a 2D list (matrix) to store the edit distances between substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first column (converting start to an empty target)
    for i in range(m + 1):
        dp[i][0] = i  # Requires 'i' deletions
        
    # Initialize the first row (converting an empty start to target)
    for j in range(n + 1):
        dp[0][j] = j  # Requires 'j' insertions
        
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if start[i - 1] == target[j - 1]:  # Characters match
                dp[i][j] = dp[i - 1][j - 1]   # No new operation needed
                
            else:  # Characters do not match
                dp[i][j] = 1 + min(dp[i -1][j],    # Deletion
                                   dp[i][j - 1],   # Insertion
                                   dp[i - 1][j - 1]# Substitution
                                )
                
    return dp[m][n]  # The edit distance between the two full strings is in the bottom-right cell

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(editdistance(s, t))
    
# How do I explain this code in an interview?
# In an interview, you can explain the code step-by-step as follows:
# 1. **Initialization**: Start by determining the lengths of the two input strings,
#    'start' and 'target'. Create a 2D list 'dp' where dp[i][j] will hold the edit distance
#    between the first i characters of 'start' and the first j characters of 'target.
# 2. **Base Cases**: Initialize the first row and first column of the 'dp' table. The first row
#    represents the edit distance when 'start' is empty (which is just the length of 'target'),
#    and the first column represents the edit distance when 'target' is empty (which is just the length of 'start').
# 3. **Filling the DP Table**: Use nested loops to fill in the rest of the 'dp' table. For each character in 'start' and 'target':
#    - If the characters match, the edit distance is the same as that of the previous characters (dp[i-1][j-1]).
#    - If the characters do not match, calculate the minimum edit distance by considering three possible operations: insertion, deletion, and substitution. Add 1 to the minimum of these three values.
# 4. **Result**: The value in dp[m][n] (where m and n are the lengths of 'start' and 'target', respectively) will give the final edit distance between the two strings.
# You can also discuss the time complexity of the algorithm, which is O(m*n) where m and n are the lengths of the two strings. The space complexity is also O(m*n) due to the 2D list used for dynamic programming.
# You can also mention edge cases, such as when one or both strings are empty, in which case the edit distance is simply the length of the other string.
# Example Input/Output:
# Input: "geek", "gesek"
# Output: 1  # Explanation: One insertion is needed to convert "geek" to "gesek".
# Input: "abc", "yabd"
# Output: 2  # Explanation: Two operations (substitution and insertion) are needed.


# What questions can I expect on this code in an interview and give me answers?
# In an interview, you might be asked the following questions about this code:
# 1. **What is the time complexity of this algorithm?**
#    - The time complexity of this algorithm is O(m*n) where m and n are the lengths of the two strings. This is because we fill in a 2D table of size (m+1) x (n+1).
# 2. **What is the space complexity of this algorithm?**
#    - The space complexity is also O(m*n) due to the 2D list used for dynamic programming. However, we can optimize it to O(min(m, n)) by only keeping track of the current and previous rows.
# 3. **Can you explain the three operations used in calculating the edit distance?**
#    - The three operations are:
#      - Insertion: Adding a character to 'start' to match 'target'.
#      - Deletion: Removing a character from 'start' to match 'target'.
#      - Substitution: Replacing a character in 'start' with a character from 'target'.
# 4. **How does the algorithm handle cases where one or both strings are empty?**
#    - If one string is empty, the edit distance is simply the length of the other string, as we would need to perform that many insertions or deletions to convert one string to the other. This is handled in the base case initialization of the 'dp' table.
# 5. **Can this algorithm be optimized further?**
#    - Yes, the space complexity can be optimized to O(min(m, n)) by only storing the current and previous rows of the 'dp' table instead of the entire table.
# 6. **What are some real-world applications of the edit distance algorithm?**
#    - The edit distance algorithm has several real-world applications, including:
#      - Spell checking: Identifying and suggesting corrections for misspelled words.
#      - DNA sequencing: Comparing genetic sequences to find similarities and differences.
#      - Natural language processing: Measuring the similarity between text strings for tasks like plagiarism detection and text similarity analysis.
