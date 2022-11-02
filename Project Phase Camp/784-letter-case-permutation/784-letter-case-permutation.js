/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function(s) {
    const res = [];
    
    const dfs = (i, s, slate) => {
//         base case
        if(i === s.length){
            res.push(slate.join(""));
            return;
        }
//         recursive case
        let char = s[i];
        if(!Number.isInteger(parseInt(char))){
//             upper case
            slate.push(char.toUpperCase());
            dfs(i + 1, s, slate);
            slate.pop();
            
//             lower case
            slate.push(char.toLowerCase());
            dfs(i + 1, s, slate);
            slate.pop();
        }else{
            slate.push(char);
            dfs(i + 1, s, slate);
            slate.pop();
        }
    }
    dfs(0,s,[]);
    return res;
};