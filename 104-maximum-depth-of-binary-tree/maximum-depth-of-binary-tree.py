class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_h=self.maxDepth(root.left)
        right_h=self.maxDepth(root.right)

        return max (left_h,right_h)+1
