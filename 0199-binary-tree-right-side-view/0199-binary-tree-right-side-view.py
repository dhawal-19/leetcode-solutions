class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            nodes = len(q)
            for i in range(nodes):
                node = q.popleft()
                if i == nodes - 1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
                
