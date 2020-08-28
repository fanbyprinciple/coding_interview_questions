//source : https://leetcode.com/problems/sort-colors/submissions/

//visualisation : https://editor.p5js.org/fanbyprinciple/present/eUaOYYh8j

// Runtime: 80 ms, faster than 50.75% of JavaScript online submissions for Sort Colors.
// Memory Usage: 37.5 MB, less than 8.16% of JavaScript online submissions for Sort Colors.


var sortColors = function(nums) {
    num_one = 0
    num_zero = 0
    num_two = 0
    for(let i=0; i<nums.length; ++i){
        if(nums[i] == 0){
            num_zero += 1
        } else if(nums[i] == 1){
            num_one += 1
        } else {
            num_two += 1
        }
    } 
    
    console.log(num_zero, num_one, num_two)
    let i = 0
    for (; i<num_zero; ++i){
        nums[i] = 0
        // if(i<num_zero){
        //     nums[i] = 0    
        // } else if(i<num_one){
        //     nums[i] = 1
        // } else if(i<num_two){
        //     nums[i] = 2
        // }
         
    }
    
    for (; i<num_zero+num_one; ++i){

        nums[i] = 1
    }
    
    for (; i<num_zero + num_one + num_two; ++i){
        nums[i] = 2
    }

   // return nums
};

//sortColors([2,0,2,1,1,0])


// better one pass
// var sortColors = function(n) {
//     let i=0, l=0, h=n.length-1;
//     while(i<=h) {
//         if(n[i]==0) {
//             [n[i], n[l]] = [n[l], n[i]];
//             i++; l++;
//         } else if(n[i]==2) {
//             [n[i], n[h]] = [n[h], n[i]];
//             h--;
//         } else i++
//     }
// };
