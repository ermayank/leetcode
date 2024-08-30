# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Breadth First Search and add to arrays
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            levelList = []
            
            for i in range(qLen):
                node = q.popleft()
                
                if node:
                    levelList.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if levelList:
                    res.append(levelList)
            
        return res