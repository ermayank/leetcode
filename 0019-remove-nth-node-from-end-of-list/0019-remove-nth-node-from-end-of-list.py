# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head
        
        # Place right node afet n postions to left node
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Place Left Pointer and Right pointer on desired locations
        while right:
            left = left.next
            right = right.next
            
        # Remove node
        left.next = left.next.next
        
        return dummyNode.next
            
        