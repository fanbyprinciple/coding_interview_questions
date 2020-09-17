//source: https://leetcode.com/problems/valid-parentheses/
//Runtime: 80 ms, faster than 55.15% of JavaScript online submissions for Valid Parentheses.
//Memory Usage: 38.3 MB, less than 14.05% of JavaScript online submissions for Valid Parentheses.

var isValid = function(s) {
    validOpen = ["(", "[", "{"]
    validClose = [")", "]", "}"]
    
    processed = []
    console.log(processed.length)
    for(let i=0;i< s.length; ++i ){
    
        if(validOpen.includes(s[i])){
            processed.push(s[i])
        }
        
        else if(validClose.includes(s[i])){
            //console.log(s[i])
            if(validOpen.indexOf(processed[processed.length-1]) == validClose.indexOf(s[i])){
               //console.log(processed[processed.length-1])
               //console.log(validOpen.indexOf(processed[processed.length-1]))
               //console.log(s[i])
               //console.log(validClose.indexOf(s[i]))
                processed.pop()
            }
            else {
                return false
            }
        }
    }
    
    if(!processed.length){
        return true
    } else {
        return false
    }
};

//isValid("(]")