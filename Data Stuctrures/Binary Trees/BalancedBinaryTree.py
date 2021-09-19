def isBalanced(self, root: TreeNode) -> bool:
    if not root:
        return True
    left=self.depth(root.left)
    right=self.depth(root.right)
    return abs(left-right)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
def depth(self,root):
    if not root:
        return 0
    return max(self.depth(root.left),self.depth(root.right))+1

