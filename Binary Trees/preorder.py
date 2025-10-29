class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def preorder(root):
    if not root:
        return []
    
    return [root.data] + preorder(root.left) + preorder(root.right)

if __name__ == "__main__":
    
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    
    print(preorder(root))