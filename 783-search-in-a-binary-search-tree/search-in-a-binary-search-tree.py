class Solution:
    def searchBST(self, root: Optional[TreeNode],target: int) -> Optional[TreeNode]:
        if root is None:
            return None

        curr=root
        while curr!=None:
            if curr.val==target:
                return curr
            elif target<curr.val:
                curr=curr.left
            else:
                curr=curr.right