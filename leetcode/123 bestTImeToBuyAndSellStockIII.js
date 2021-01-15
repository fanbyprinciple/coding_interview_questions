/**
 * @param {number[]} prices
 * @return {number}
 */


// refer ence 1 : understanding: https://www.youtube.com/watch?v=0FKn0FSIQYE
// reference 2 : code : https://github.com/chihungyu1116/leetcode-javascript/blob/master/123%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20III.js

// we need to choose a combination of two buys and sell to amximise profit
// The reason we can't make this trivial i.e.
// finding min and max is because then we might maximise on first buy (which works in example 2 ) and sell but not on second

var maxProfit = function(prices) {
    let n = prices.length
    
    
    //let p1 = prices[0]
    //let p2 = prices[n-1]
    
    let profit1 = []
    let profit2 = []
    
    
    // We are going for more brute force approach here
    // we are creating two array one from start to ginish
    //another from finish to start and calculating all possible combinations of profit
    // and then finally returning the max
    
    // || 0 because if profit is undefined we take it as 0
    
    let min = prices[0]
    for (let i =0; i<n; ++i){
        
        // getting max profit from 0 to x
        min = Math.min(prices[i], min)
        profit1[i] = Math.max(profit1[i-1] || 0, prices[i] - min)
        //console.log(p1)
    }
    
    let max =prices[prices.length-1]
    for(let i=n-2; i>=0; i--){
        // getting max profit from i+1 to end
        max = Math.max(prices[i], max)
        profit2[i] = Math.max(profit2[i+1] || 0, max - prices[i])
    
    }
    
    
    var maxProfit = 0;
    for(x = 0; x < prices.length; x++) {
        var maxProfitSeperateAtX = (profit1[x] || 0) + (profit2[x] || 0);
        maxProfit = Math.max(maxProfitSeperateAtX, maxProfit);
    }
    
    return maxProfit;
    
    
};

//testing testing 123
let a = [3,3,5,0,0,3,1,4]
console.log(maxProfit(a))

// console.log(maxProfit([3,3,5,0,0,3,1,4]))

 /*

solution by sujatat tiwari doesn't work


var maxProfit = function(prices) {
    if (prices.length ==0){
        return 0
    }
    let fb = Number.MIN_VALUE // first buy
    let sb = Number.MIN_VALUE // second buy
    let fs = 0 // first sell
    let ss = 0 // second sell
    
    console.log(fb)
    
    for (let i=0; i< prices.length; i++){
        fb = Math.max(fb, -prices[i]) 
        // because we are just paying here and have no money with us
        fs = Math.max(fs, fb + prices[i])
        // since now we have money after first buy and we get profit so plus
        sb = Math.max(sb, fs -prices[i]) // similar logic
        ss = Math.max(sb, sb + prices[i])
        
    }

    return ss
    
    
};

*/