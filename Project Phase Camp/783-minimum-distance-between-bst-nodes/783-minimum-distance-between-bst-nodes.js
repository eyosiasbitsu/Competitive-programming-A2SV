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
var minDiffInBST = function(root) {
    
    const walk = (node) => {
        if(node === null){
            return [];
        }
        
        const left = walk(node.left);
        const right = walk(node.right);
        
        let temp = left.concat([node.val]);
        let cur = temp.concat(right);
        
        return cur;
    };
    
    let ar = walk(root);
    let ans = Infinity;
    console.log(ar);
    for(let i = 0; i < ar.length - 1; i++){
        ans = Math.min(ar[i + 1] - ar[i], ans);
    }
    
    return ans;
};