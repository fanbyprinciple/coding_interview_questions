# source: https://leetcode.com/problems/roman-to-integer/submissions/

# Runtime: 64 ms, faster than 21.38% of Python online submissions for Roman to Integer.
# Memory Usage: 12.8 MB, less than 35.05% of Python online submissions for Roman to Integer.

def romanToInt( s):
        """
        :type s: str
        :rtype: int
        """
        
        rome_dict = {"I":1, "V":5,"X":10,"L":50, "C":100, "D":500, "M":1000 }

        sum = 0
        #arr_i = []
        for i in range(0, len(s)-1):
            
            print(s[i])
            if (rome_dict[s[i]]>=rome_dict[s[i+1]]):
                
                sum += rome_dict[s[i]]
                #print("positive ", s[i],rome_dict[s[i]],s[i+1],rome_dict[s[i+1]], " sum ", sum)

            else :
                
                sum -= rome_dict[s[i]]
                #sum += rome_dict[s[i+1]]
                #print("negative ", s[i],rome_dict[s[i]],s[i+1], rome_dict[s[i+1]], " sum ", sum)
                #i = i+1
                
        #print(s[i])
        sum += rome_dict[s[-1]]
        ### adding the last
        return sum
            

print(romanToInt("LVIII"))