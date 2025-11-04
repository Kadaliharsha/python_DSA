from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
        
def rootToNodePath(root):
    if not root:
        return []
    
    queue = deque([(root, [root.data])])
    result = []
    
    while queue:
        node, path = queue.popleft()
        
        if not node.left and not node.right:
            result.append(path)
            
        if node.left:
            queue.append((node.left, path + [node.left.data]))
            
        if node.right:
            queue.append((node.right, path + [node.right.data]))
            
    return result

if __name__ == "__main__":
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Root to Node Paths:", rootToNodePath(root))
    
# Time complexity: O(n) --> We visit each node exactly once.
# Space complexity: O(H) --> In the worst case, the queue can store all nodes at the deepest level of the tree, which is proportional to the height of the tree.