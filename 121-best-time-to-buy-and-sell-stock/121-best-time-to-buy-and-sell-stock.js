/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    var cur = prices[0];
    var profit = 0;
    
    for(var i = 0; i < prices.length; i++){
        if(prices[i] < cur){
            cur = prices[i];
        }
        else{
            let temp = Math.max(prices[i]-cur,profit);
            profit = temp;
        }
    }
    return profit
};