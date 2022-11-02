/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    const neg = [];
    const pos = [];
    
    for(let item of nums){
        if(item < 0){
            neg.push(item);
        }else{
            pos.push(item);
        }
    }
    
    let n = 0;
    let p = 0;
    
    let fn = false;
    let fp = true;
    
    let res = [];
    
    while(n + p < nums.length){
        if(fn){
            res.push(neg[n]);
            n += 1;
            fn = false;
            fp = true
        }else{
            res.push(pos[p]);
            p += 1;
            fn = true;
            fp = false;
        }
    }
    
    return res;
};