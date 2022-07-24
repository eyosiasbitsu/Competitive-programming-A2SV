/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let r = matrix.length - 1;
    let c = 0;
    
    while(r >= 0 && c < matrix[0].length){
        if(matrix[r][c] > target) r -= 1;
        else if(matrix[r][c] < target) c += 1;
        else return true;
    }
    return false;
};