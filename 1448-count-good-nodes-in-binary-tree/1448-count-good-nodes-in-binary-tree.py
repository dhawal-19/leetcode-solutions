class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0 
        q = deque([[root,root.val]])
        while q:
            node,max_val = q.popleft()
            if node.val >= max_val:
                max_val = node.val
                ans += 1
            if node.left:
                q.append([node.left,max_val])
            if node.right:
                q.append([node.right,max_val])
        return ans


        