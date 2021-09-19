def validBST(self,root,minnode,maxnode):
    if not root:
        return True
    val=root.val
    if val<=minnode or val>=maxnode:
        return False
    if not self.validBST(root.left,minnode,val):
        return False
    if not self.validBST(root.right,val,maxnode):
        return False
    return True
def isValidBST(self, root: TreeNode) -> bool:
    return self.validBST(root,float('-inf'),float('inf'))
   
