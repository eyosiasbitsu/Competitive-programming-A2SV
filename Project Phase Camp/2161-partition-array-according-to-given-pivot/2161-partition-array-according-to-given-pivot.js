/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    const less = [];
    const greater = [];
    const equal = [];
    
    for(item of nums){
        if(item > pivot){
            greater.push(item);
        }else if(item < pivot){
            less.push(item);
        }
        else{
            equal.push(item);
        }
    }
    return less.concat(equal).concat(greater);
};