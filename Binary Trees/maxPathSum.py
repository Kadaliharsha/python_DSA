class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
        
def maxPathsum(root):
    maxS = float('-inf')

    def helper(node):
        nonlocal maxS
        if not node:
            return 0

        left = max(0, helper(node.left))
        right = max(0, helper(node.right))

        maxS = max(maxS, node.data + left + right)

        return node.data + max(left, right)

    helper(root)
    return maxS

if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(9)
    root.right = TreeNode(-10)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Max Sum:", maxPathsum(root))