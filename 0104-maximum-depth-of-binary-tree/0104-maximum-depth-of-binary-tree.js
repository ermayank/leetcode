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
 * @return {number}
 */
var maxDepth = function(root) {
  depthMax = 0

  //Depth First Search
  function dfs(root, depth){
    if(!root){
      depthMax = Math.max(depthMax, depth)
      return;
    }
    dfs(root.left, depth + 1);
    dfs(root.right, depth + 1);
  }

  dfs(root, 0)
  return depthMax;
};