# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Breadth First Search Approach
        
        res = []
        q = collections.deque([root])
        
        while q:
            rightNode = None
            qLen = len(q)
            
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    rightNode = curr
                    q.append(curr.left)
                    q.append(curr.right)
            
            if rightNode:
                res.append(rightNode.val)
            
        return res
                    
                
            
        