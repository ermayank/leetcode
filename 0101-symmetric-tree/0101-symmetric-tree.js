/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    
    if(!root) {return false}
    
    return isSame(root.left, root.right)
    
    function isSame(p,q){
        if(!p && !q) {return true}
        if(!p || !q || p.val !== q.val) {return false}
        
        //Compare Left subtree of p to right subtree of q
        //Compare right subtree of p to left subtree of q
        
        return isSame(p.left, q.right) && isSame(p.right, q.left)
    }
    
    
};