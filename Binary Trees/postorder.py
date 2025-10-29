class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
        
def postorder(root):
    if not root:
        return []
    
    return postorder(root.left) + postorder(root.right) + [root.data]

if __name__ == "__main__":
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(4)
    
    print(postorder(root))