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
var getMinimumDifference = function(root) {
    let res = Infinity;
    
    const walk = (node) => {
        if(node === null){
          return [Infinity, -Infinity];
        }
        
        const [minleft, maxleft] = walk(node.left);
        const [minright, maxright] = walk(node.right);
        
        res = Math.min(res, 
                       Math.abs(maxleft - node.val),
                       Math.abs(minright - node.val));
        
        return [Math.min(node.val, minleft), Math.max(node.val, maxright)];
        
    };
    
    walk(root);
    return res
};