
class Solution:
    def __init__(self):
        self.ans=True

    def height(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0

        left_h=self.height(root.left)
        right_h=self.height(root.right)

        if abs(left_h-right_h)>1:
            self.ans=False

        return max(left_h,right_h)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans
        