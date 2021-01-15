//https://leetcode.com/problems/running-sum-of-1d-array/submissions/
//Runtime: 76 ms, faster than 81.60% of JavaScript online submissions for Running Sum of 1d Array.
//Memory Usage: 38.9 MB, less than 5.04% of JavaScript online submissions for Running Sum of 1d Array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let result = [nums[0]]
    for(let i=1; i<nums.length; ++i){
        result.push(nums[i] + result[i-1])
    }
    return result
};