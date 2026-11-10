# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        result = [0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            
            if count[0] == 1:
                result[0] = node.val
            count[0] = count[0] - 1

            if count[0] > 0:
                dfs(node.right)
        
        dfs(root)
        return result[0]