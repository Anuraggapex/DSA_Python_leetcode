class Solution:
    def __init__(self):
        self.ans=[]
    def postorder(self,root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.postorder(root)
        return self.ans
        