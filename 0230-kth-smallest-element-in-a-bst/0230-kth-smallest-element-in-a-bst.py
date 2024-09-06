# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder Traversal Recursive
        res = []
        
        def dfsInorder(node):
            if not node:
                return
            
            dfsInorder(node.left)
            
            res.append(node.val)
            if len(res) == k:
                return
            dfsInorder(node.right)
        
        dfsInorder(root)
        return res[k-1]
        
        
        
        