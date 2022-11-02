/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
//     global result
    const res = [];
    
//     dfs recursive helper
    const dfs = (i, nums, slate) => {
//         base case
        if(i === nums.length){
            let temp = slate.slice();
            res.push(temp);
            return;
        }
//         dfs recursive case
        dfs(i + 1, nums, slate);
        slate.push(nums[i]);
        dfs(i + 1, nums, slate);
        slate.pop();
    }
    dfs(0, nums, []);
    return res;
};