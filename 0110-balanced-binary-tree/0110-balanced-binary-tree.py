# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True,0]
            lh = dfs(root.left)
            rh = dfs(root.right)
            balanced = True if abs(lh[1] - rh[1]) <= 1 and lh[0] and rh[0] else False
            return [balanced,1 + max(lh[1],rh[1])]
        return dfs(root)[0]