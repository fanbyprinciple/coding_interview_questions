/// source: https://leetcode.com/problems/implement-strstr/submissions/

// Runtime: 5516 ms, faster than 5.06% of JavaScript online submissions for Implement strStr().
// Memory Usage: 40.3 MB, less than 5.03% of JavaScript online submissions for Implement strStr().


/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    
    if(needle == ""){
            return 0
        }
    
      
    found = true
    for(let i=0; i< haystack.length;++i){
        if(haystack[i] === needle[0]){
            found = true
            for(let j=0; j< needle.length; ++j){
              if(haystack[i+j] != needle[j]){
                  found = false
              }
           }
           
           if(found){
                return i
           }
   
        }
    }
  
    return -1
  };