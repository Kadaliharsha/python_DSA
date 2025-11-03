from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def topview(root):
    if not root:
        return []
    
    queue = deque([(root, 0)])
    hd_map = {}
    
    while queue:
        node, hd = queue.popleft()
        
        if hd not in hd_map:
            hd_map[hd] = node.data
            
        if node.left:
            queue.append((node.left, hd - 1))
            
        if node.right:
            queue.append((node.right, hd + 1))
            
    return [hd_map[x] for x in sorted(hd_map.keys())]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Top view of the binary tree is:", topview(root))
    
# Time complexity: O(n) --> How: We visit each node exactly once in the BFS traversal.
# Space complexity: O(n) --> How: In the worst case, the queue and hd_map can store all nodes in the tree.