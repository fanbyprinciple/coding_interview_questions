// Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
// Type: ??
// Time Complexity: ??
// Space Complexity: ??

/*
Runtime: 304 ms, faster than 26.08% of JavaScript online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 43.4 MB, less than 25.10% of JavaScript online submissions for Longest Substring Without Repeating Characters.
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