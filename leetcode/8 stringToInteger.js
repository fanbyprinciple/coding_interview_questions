// Source : https://leetcode.com/problems/string-to-integer-atoi/submissions/
// Runtime: 148 ms, faster than 14.01% of JavaScript online submissions for String to Integer (atoi).
// Memory Usage: 43.3 MB, less than 5.02% of JavaScript online submissions for String to Integer (atoi).

var myAtoi = function(str) {
    numberArray = "1234567890"
    sign = "-+"
    processed = []
    for(let i=0; i <str.length; ++i){

        if(!(str[i] == " " && processed.length ==0) ){
            
            if(numberArray.includes(str[i]) || (sign.includes(str[i])&&processed.length==0)){
                console.log(str[i])        
                processed.push(str[i])
                
                
            } else {
                
                if(processed.length == 0){
                    return 0
                } else if(processed.length == 1 && sign.includes(processed[0])) {
                    return 0
                } else {
                    
                    let res = parseInt(processed.join(""))
                    if(res > 2**31-1){
                        res = 2**31-1
                    } else if (res < -(2**31)){
                        res = -(2**31)
                    } 
                             
                    //console.log(processed.join(""))
                    return res
                    
                }
            }
        
        }
    }

    if(processed.length == 0){
        return 0
    } else if(processed.length == 1 && sign.includes(processed[0])) {
        return 0
    } else {
        
        let res = parseInt(processed.join(""))
        if(res > 2**31-1){
            res = 2**31-1
        } else if (res < -(2**31)){
            res = -(2**31)
        } 
                 
        //console.log(processed.join(""))
        return res
        
    }
    
};

// myAtoi("-")