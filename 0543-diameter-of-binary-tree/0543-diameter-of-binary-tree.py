# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(root):
            nonlocal result
            if not root: return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            result = max(result,lh + rh)
            return 1 + max(lh,rh)
        dfs(root)
        return result