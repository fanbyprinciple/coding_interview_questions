# Source : https://leetcode.com/problems/generate-parentheses/discuss/?currentPage=1&orderBy=hot&query=


## Recursive brilliance 
# not mine 

def generateParenthesis(self, n: int) -> List[str]:
        #initialise res to store result
        res = []
        
        #Backtracking function where we take input as the string of paranthesis, n, num of opening paras and num of closing paras
        def generate_paranthesis(s, n, open_para, close_para):
            
            #Base case... if the length of s == 2*n we append the result and return. We use 2*n because we need to add paranthesis pairs
            if len(s)==n*2:
                res.append(s)
                return
            
            #if opening paranthesis <n, we add an opening paranthesis
            if open_para<n:
                generate_paranthesis(s+"(", n, open_para+1, close_para)
                
            #If closing paranthesis <opening paranthesis .. this is because we cannot have a closing paranthesis before opening one    
            if close_para<open_para:
                generate_paranthesis(s+")", n, open_para, close_para+1)
        
        generate_paranthesis("", n, 0, 0)
        return(res)

### MY WRONG ATTEMPT
# def generateParenthesis(n):
#     solutionSet = []
    
#     for i in range(0, n+1):
#         current = ""
#         for j in range(0,n-i):
#             current += "("
#         for j in range(j, len(current)+1):
#             current += ")"
#         solutionSet.append(current)

#     return solutionSet

# print(generateParenthesis(3))

'''
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

