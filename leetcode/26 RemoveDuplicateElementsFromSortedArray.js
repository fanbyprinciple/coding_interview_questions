// source : https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

//Pretty bad score i guess
// Runtime: 212 ms, faster than 13.15% of JavaScript online submissions for Remove Duplicates from Sorted Array.
// Memory Usage: 39.2 MB, less than 32.10% of JavaScript online submissions for Remove Duplicates from Sorted Array.

var removeDuplicates = function(nums) {
    nList = []
    for(i=0; i< nums.length; ++i){
        if (!nList.includes(nums[i])){
            nList.push(nums[i])
        }
    }
        
    
    for (i=0; i< nList.length; ++i){
        nums[i] = nList[i]
    }
    
    return nList.length
};

//removeDuplicates(['1','1','2'])

// best answer

// let removeDuplicates = function(nums) {
//     if (!nums.length) {
//       return 0;
//     }
  
//     let pointer1 = 0;
//     for (let pointer2 = 1; pointer2 < nums.length; pointer2++) {
//       if (nums[pointer1] !== nums[pointer2]) {
//         pointer1++;
//         nums[pointer1] = nums[pointer2];
//       }
//     }
  
//     return pointer1 + 1;
//   };