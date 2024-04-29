/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let curr = head;
    let prev = null;
    let next;
    
    while(curr != null){
        next = curr.next;    // curr.next node is saved in next
        curr.next = prev;    // current node is made to point previous
        prev = curr;         // prev node is now curr for next iteration
        curr = next;         // current node is made next for next iteration
    }
    return prev;
};