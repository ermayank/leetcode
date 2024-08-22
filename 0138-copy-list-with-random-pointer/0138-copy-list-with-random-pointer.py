"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldNodeToNewMap = { None : None }
        
        # Make HashMap
        curr = head
        while curr:
            copyNode = Node(curr.val)
            oldNodeToNewMap[curr] = copyNode
            curr = curr.next
        
        # Make linkes
        curr = head
        while curr:
            copyNode = oldNodeToNewMap[curr]
            copyNode.next = oldNodeToNewMap[curr.next]
            copyNode.random = oldNodeToNewMap[curr.random]
            curr = curr.next
        
        return oldNodeToNewMap[head]
        