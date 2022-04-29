var twoSum = function(nums,target){
    for(var i = 0; i<nums.length;i++){
        var expected = target - nums[i];
        if(nums.includes(expected)&&nums.indexOf(expected) !== i){
            return [i,nums.indexOf(expected)];
            }
        }
    return []
}