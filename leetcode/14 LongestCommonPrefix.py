# Source: https://leetcode.com/problems/longest-common-prefix/
# Type: ??
# Time Complexity: ??
# Space Complexity: ??

# Runtime: 36 ms, faster than 67.64% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.8 MB, less than 87.93% of Python3 online submissions for Longest Common Prefix.

# MY SUBMISSION

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # minLength = float('inf')
        # for i in str:
        #     if(len(i)< minLength):
        #         minlength = len(i)

        commonElement = "" # This we need to return
        i =0
        try:
            while(True):
                currentElement = strs[0][i]
                # the character under consideration
                #print(currentElement)
                flag = 1
                for element in strs:
                    if(currentElement != element[i]):
                        flag = 0
                if(flag == 0):
                    return commonElement
                else:
                    commonElement += strs[0][i]
                    i+=1

        except:
            # try except so as to avoid calculating minLength
            # at the beginning
            # at the end of any of the string when exception is raised
            # it will simply return the commonElement
            return commonElement

    


# print(longestCommonPrefix(["flower","flow","flight"]))