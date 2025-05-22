class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val
        def dfs(root):
            nonlocal cnt,res
            if not root: return
            dfs(root.left)
            cnt -= 1
            if cnt == 0:
                res = root.val
                return
            dfs(root.right)
        dfs(root)
        return res