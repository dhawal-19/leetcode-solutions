class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return arr[k - 1]