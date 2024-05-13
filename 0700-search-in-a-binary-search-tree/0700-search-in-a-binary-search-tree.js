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
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function(root, val) {
    if(root == null)return null
    
    let currentNode = root;
   
    while(currentNode){
        if(val > currentNode.val){currentNode = currentNode.right}
        else if(val < currentNode.val){currentNode = currentNode.left}
        else{return currentNode}
    }
    return null;
};