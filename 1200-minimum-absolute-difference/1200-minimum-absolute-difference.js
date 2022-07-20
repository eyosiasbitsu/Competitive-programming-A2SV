/**
 * @param {number[]} arr
 * @return {number[][]}
 */
var minimumAbsDifference = function(arr) {
    arr.sort((a,b)=> a - b);
    const res = [];
    let min = Infinity;
    
    for(let i = 0; i < arr.length - 1; i++){
        let dif = arr[i + 1] - arr[i];
        min = Math.min(dif, min);
    }
    
    for(let i = 0; i < arr.length - 1; i++){
        let dif = arr[i + 1] - arr[i];
        if(min === dif){
            res.push([arr[i], arr[i + 1]]);
        }
    }
    return res
};