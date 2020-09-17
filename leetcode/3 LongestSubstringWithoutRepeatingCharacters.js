// Source: https://leetcode.com/problems/longest-substring-without-repeating-characters
// Type: String, Sliding Window
// Time Complexity: O(N^2) (brute force), O(N) (sliding window)
// Space Complexity: ??

/*
Runtime: 36 ms, faster than 67.64% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.8 MB, less than 87.93% of Python3 online submissions for Longest Common Prefix.
*/


var lengthOfLongestSubstring = function(s = "pwwkew") {
    let megaLongest = ""
    let longest = ""
    
    for(let j=0; j < s.length; ++j){
        longest += s[j]
        
        for(let i=j+1; i <s.length; ++i){
            //console.log(s[i], longest)
            
            if(!(longest.includes(s[i])) ){
                console.log("s[i]", s[i])
                longest += s[i]
            
            } else {
                break
            }
        }
        if(longest.length > megaLongest.length) {
            //console.log("Longest length : ",longest.length)
            
            megaLongest = longest
        }
        longest = ""
    }
        
    return megaLongest.length
    
};

/* BETTER SOLUTION
sliding window

var lengthOfLongestSubstring = function(s) {
    if(s.length <= 1) return s.length; 
    
    let leftPointer = 0; 
    let container = []; 
    
    let max = 1;
    
    for(let i = 1; i < s.length; i++){
        let container = s.substring(leftPointer, i);
        if(container.includes(s[i])){
            leftPointer = leftPointer + container.indexOf(s[i]) + 1;
        }
        container = s.substring(leftPointer, i+1);
        max = max >= container.length ?  max : container.length;        
    }
    return max;     
};

*/
