# one way to  optimise this could be to use 
# some other implementation to reverse other than using array[::-1]
# 26ms

class Solution:
    def reverse(self, x: int) -> int:
        
        if(x>=0):
            result = int(str(x)[::-1]) 

        else:
            b = str(x)[1:]
            result = int("-" + str(int(b[::-1])))
        
        if (result>= 2147483647 or result <=- 2147483648):
            return 0
        else:
            return result
            
        
            
## alt SOLUTION
## 36 ms
## can be improved by removing range

# class Solution:
#     def reverse(self, x: int) -> int:
#         rem = 0
#         quo=x
#         if(quo<0):
#             quo=quo*(-1)
#         while (quo > 9):
#             rem = rem*10 +quo % 10
#             quo=quo//10
#         if(quo<10):
#             rem = rem * 10 + quo % 10
#         if(x<0):
#             rem=rem*(-1)
#         if(rem not in range(-2**31, (2**31))):
#             return 0
#         else:
#             return rem

