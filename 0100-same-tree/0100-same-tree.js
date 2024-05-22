/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */

var isSameTree = function(p, q) {
  //Base Casees
  if(p == null && q == null) {return true};
  if(p == null || q == null) {return false};
   	
  //Recurssive
  if (p.val == q.val){return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)}
  
  return false
};