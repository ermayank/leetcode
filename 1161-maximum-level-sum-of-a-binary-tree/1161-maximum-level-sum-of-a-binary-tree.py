# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum, maxLevel, level = -float('inf'), 0, 0
        q = collections.deque()
        q.append(root)
        
        while q:
            level += 1
            qLen = len(q)
            levelSum = 0
            
            for i in range(qLen):
                node = q.popleft()
                levelSum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if maxSum < levelSum:
                maxSum, maxLevel = levelSum, level
        return maxLevel

                
        