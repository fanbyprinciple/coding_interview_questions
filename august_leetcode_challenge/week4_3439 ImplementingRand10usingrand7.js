// It uses something called rejection sampling 
// find it here: https://leetcode.com/problems/implement-rand10-using-rand7/solution/
// practical explanation : https://leetcode.com/problems/implement-rand10-using-rand7/discuss/817188/JavaScript-with-beginners'-explanation-of-math

// //rejected answer of mine
// var rand10 = function() {
//     sum = 0
//     for(let i=0; i<10; ++i){
//         sum += rand7()
//     }
    
//     return Math.floor(sum/7)
    
// };


const rand10 = () => {
    let random = 41;
    while (random > 40) random = 7 * (rand7() - 1) + rand7();
    return (random % 10) + 1; 
};


//  return (rand7() + rand7() + rand7() + rand7() + rand7()) % 10 + 1; also works
