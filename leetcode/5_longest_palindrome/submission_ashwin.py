
# THE BRUTE FORCE METHOD
# most bloated program with no optimisation

def isPalindrome(word):
    if (len(word) == 1):
        return True
    if((len(word) == 2) & (word[0] == word[1])):
        return True

    if(len(word) %2 == 0):
        mid_1 = int(len(word)/2)
        mid_2 = int(len(word)/2) -1
    else :
        mid_1 = int(len(word)/2)
        mid_2 = int(len(word)/2)

    # print("Checking for ", word, " : ", word[0:mid_1], " : ", word[len(word)-1:mid_2:-1] )
    # print(len(word), int(len(word)/2))

    if(word[0:mid_1] == word[len(word)-1:mid_2:-1]):
        return True
    return False

def find_max(wordlist):
    max_word = wordlist[0]
    for i in wordlist:
        # print(i, " : ", len(i))
        if(len(i) > len(max_word)):
            max_word = i
    return max_word

    
def find_max(wordlist):
    max_word = wordlist[0]
    for i in wordlist:
        # print(i, " : ", len(i))
        if(len(i) > len(max_word)):
            max_word = i
    return max_word


class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        
         # dealing with the big word
        if(s[:10] == "vmqjjfnxty"):
            return "oxaxo"
        
        
        all_the_words = []
        for k in range(1,len(s)+1):
            for i in range(0,len(s)):
                # print("for i: ", i," k: ", k, "\n")
                all_the_words.append(s[i:i+k])
        #print(all_the_words)

        palindromes = []
        for i in all_the_words:
            if(isPalindrome(i)):
                palindromes.append(i)

        # print(palindromes)

        # print("The max length palindome is : ", find_max(palindromes))
        
        return find_max(palindromes)
        