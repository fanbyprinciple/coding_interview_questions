class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
#         currSubString = ''
#         for i in s[:len(s)//2]:
#             currSubString += i
#             multiply = len(s)//len(currSubString)
#             if currSubString * multiply == s:
#                 return True
#         return False

#         time complexity optimal solution
#         return (s + s)[1:-1].find(s) != -1
