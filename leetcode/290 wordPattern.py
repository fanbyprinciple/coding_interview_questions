# Source: https://leetcode.com/problems/word-pattern/
# Time Complexity: O(n)
# Type: Hash Table

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        patternToWord = {}
        wordToPattern = {}
        words = str.split()
        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):
            return False
        for i, c in enumerate(pattern):
            word = words[i]
            if c not in patternToWord and word not in wordToPattern:
                patternToWord[c] = word
                wordToPattern[word] = c
            if c not in patternToWord or patternToWord[c] != word:
                return False
            if word not in wordToPattern or wordToPattern[word] != c:
                return False
        return True
                
            
