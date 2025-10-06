# Largest sum cycle

def largestsumcycle(edges):
    n = len(edges) # size of the graph
    visited = [0] * n # we can consider states as 0 - unvisited, 1 - visiting, 2 - fully processed
    max_sum = -1  # this will be our answer
    
    for i in range(n): # if the node is processing we skip
        if visited[i] != 0:
            continue
        
        path = {} # We can keep track of the order
        u = i # starting from node i
        
        while u != -1 and visited[u] == 0:
            path[u] = True # Since we visiting we update the path
            visited[u] = 1 # mark as visiting
            u = edges[u] # we move to the next node
            
        if u != -1 and visited[u] == 1: # if a cycle is detected
            cycle_sum = 0
            start = u
            cycle_sum += start
            v = edges[start]
            
            while v != start:
                cycle_sum += v
                v = edges[v]
                
            max_sum = max(max_sum, cycle_sum)
            
        for node in path:
            visited[node] = 2
    
    return max_sum

# correct the code or comments if any problem


if __name__ == "__main__":
    e = list(map(int, input().split()))
    print(largestsumcycle(e))
    
# give me a script so that I can explain this in a interview
# The function largestsumcycle takes a list of integers 'edges' as input, where each index represents a node and the value at that index represents the next node it points to. The goal is to find the largest sum of values in any cycle present in the graph formed by these edges.

# How do I explain this code in an interview?
# In an interview, you can explain the code step-by-step as follows:
# 1. **Initialization**: Start by initializing the number of nodes 'n' and a 'visited' list to keep track of the state of each node (unvisited, visiting, or fully processed). Also, initialize 'max_sum' to -1 to store the maximum cycle sum found.
# 2. **Outer Loop**: Iterate through each node in the graph. If a node has already been fully processed (visited[u] == 2), skip it.
# 3. **Path Tracking**: For each unvisited node, use a dictionary 'path' to track the nodes in the current traversal. This helps in identifying cycles.
# 4. **Cycle Detection**: Use a while loop to traverse the graph starting from the current node. Mark nodes as visiting (visited[u] == 1) and add them to the 'path'. If you encounter a node that is already being visited, a cycle is detected.
# 5. **Cycle Sum Calculation**: If a cycle is detected, calculate the sum of the nodes in the cycle. Start from the detected node and keep adding the values until you return to the starting node.
# 6. **Update Maximum Sum**: Compare the calculated cycle sum with 'max_sum' and update it if the current cycle sum is greater.
# 7. **Mark Nodes as Processed**: After processing the current path, mark all nodes in the path as fully processed (visited[node] == 2).
# 8. **Return Result**: Finally, return the maximum cycle sum found, or -1 if no cycles were detected.
# You can also discuss the time complexity of the algorithm, which is O(n) since each node is processed at most twice (once during the initial traversal and once when marking as fully processed).
# You can also mention edge cases, such as when there are no cycles in the graph, in which case the function will return -1.

# Example Input/Output:
# Input: 1 2 0 -1
# Output: 3  # Explanation: The cycle is 0 -> 1 -> 2 -> 0, and the sum is 0 + 1 + 2 = 3.

# What questions can I expect on this code in an interview and give me answers?
# In an interview, you might be asked the following questions about this code:
# 1. **What is the time complexity of this algorithm?**
#    - The time complexity of this algorithm is O(n) since each node is processed at most twice (once during the initial traversal and once when marking as fully processed).

# 2. **What is the space complexity of this algorithm?**
#    - The space complexity is O(n) due to the 'visited' list and the 'path' dictionary used to track the nodes in the current traversal.

# 3. **How does the algorithm handle cycles in the graph?**
#    - The algorithm detects cycles by using a 'path' dictionary to track nodes currently being visited. If it encounters a node that is already in the 'path', it indicates a cycle, and the algorithm then calculates the sum of the nodes in that cycle.

# 4. **What happens if there are no cycles in the graph?**
#    - If there are no cycles in the graph, the function will return -1, indicating that no cycles were found.

# 5. **Can this algorithm handle negative values in the edges?**
#    - Yes, the algorithm can handle negative values in the edges. The cycle sum is calculated based on the actual values of the nodes, so negative values will be included in the sum if they are part of a cycle.

# 6. **What if the input list is empty?**
#    - If the input list is empty, the function will return -1 since there are no nodes to form any cycles.

# 7. **How would you modify the algorithm to return the actual cycle with the largest sum instead of just the sum?**
#    - To return the actual cycle with the largest sum, you could store the nodes of the cycle in a separate list when you detect a cycle. When updating 'max_sum', also update a variable to store the current cycle's nodes. Finally, return both the maximum sum and the corresponding cycle.

# 8. **What are some potential edge cases to consider when testing this function?**
#    - Some potential edge cases include:
#      - Graphs with only one node (self-loop)
#      - Graphs with multiple disconnected components
#      - Graphs where all nodes point to a single node (star topology)
#      - Graphs with negative cycles

# 9. **How does the algorithm ensure that it doesn't revisit nodes unnecessarily?**
#    - The algorithm uses the 'visited' list to track the state of each node. Nodes are marked as unvisited (0), visiting (1), or fully processed (2). This prevents unnecessary revisits to nodes that have already been fully processed.

# 10. **Can this algorithm be applied to directed graphs only, or can it handle undirected graphs as well?**
#    - This algorithm is designed for directed graphs, as it follows the direction of edges from one node to another. For undirected graphs, the approach would need to be modified to account for bidirectional edges and avoid counting cycles multiple times.


# I want the list of coding questions that I can expect in the interview
# Here are some coding questions you might expect in your interview with Juspay:
# 1. **Array and String Manipulation**:
#    - Find the maximum sum of a contiguous subarray (Kadane's Algorithm).
#    - Reverse a string or an array in place.
#    - Check if two strings are anagrams of each other.

# 2. **Linked Lists**:
#    - Reverse a linked list.
#    - Detect a cycle in a linked list (Floyd’s Tortoise and Hare).
#    - Find the middle element of a linked list.

# 3. **Trees and Graphs**:
#    - Implement depth-first search (DFS) and breadth-first search (BFS).
#    - Find the lowest common ancestor (LCA) of two nodes in a binary tree.
#    - Check if a binary tree is balanced.
#    - Find the largest sum cycle in a directed graph (as in the provided code).
#    - Detect cycles in a directed graph using DFS.

# 4. **Dynamic Programming**:
#    - Solve the 0/1 Knapsack problem.

