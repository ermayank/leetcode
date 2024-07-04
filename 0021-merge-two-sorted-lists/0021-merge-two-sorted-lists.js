/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    
    let dummy = tail = new ListNode
    
    while(list1 && list2){
        const isList2Greater = list1.val <= list2.val
        
        if(isList2Greater){
           tail.next = list1
            list1 = list1.next
           }
        else{
            tail.next = list2
            list2 = list2.next
        }
        
        tail = tail.next
        
    }
    tail.next = list1 || list2;
    
    return dummy.next
};